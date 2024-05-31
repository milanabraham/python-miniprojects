# yt_download_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yt_download_project.urls')),  # Include app's URLs
]
