from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from upload.models import profile
from upload.serializers import ProfileSerializer


class proListView(APIView):
    def get(self, request):
        pro = profile.objects.all()
        pro_serializer = ProfileSerializer(pro, many=True)
        resp1 = {
            "code": 1,
            "message": "success",
            "result": pro_serializer.data
        }

        return Response(data=resp1, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp2 = {
                "code": 1,
                "message": "success",
                "result": serializer.data
            }
            return Response(resp2, status=status.HTTP_201_CREATED)
        else:
            resp3 = {
                "code": 0,
                "message": "Unsuccess",
                "result": serializer.errors
            }
            return Response(resp3)