from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #will need to restructure this eventually
    path('eplus_submission', views.index, name='eplus_submission'),
    path('process_zip', views.process_zip, name='file_upload'),
    path('eplus_processes', views.eplus_processes, name='running processes'),
    path('Test_Exp', views.Test, name='test'),
]
