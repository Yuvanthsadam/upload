from django.urls import path
from upload.views import proListView, proDetailView

path('profile', proListView.as_view(), name='pro-list'),
path('list/<int:pk>', proDetailView.as_view(), name='emp-detail'),
