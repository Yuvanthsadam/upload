from django.contrib import admin
from django.urls import path
# from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from upload.views import proListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile', proListView.as_view(), name='pro-list'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)