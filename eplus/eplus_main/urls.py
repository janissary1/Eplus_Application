from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_zip', views.process_zip, name='file_upload'),
]
