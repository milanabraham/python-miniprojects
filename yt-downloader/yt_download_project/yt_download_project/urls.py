# yt_download_project/yt_download_project/urls.py

from django.urls import path
from . import views  # Import your view functions

urlpatterns = [
    path('', views.index, name='index'),  # Map URL pattern to view function
    path('download/', views.download, name='download'),
]
