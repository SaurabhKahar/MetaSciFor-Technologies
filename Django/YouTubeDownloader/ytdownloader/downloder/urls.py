from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the index view
    path('download/', views.download, name='download'),  # Maps '/download/' to the download view
]