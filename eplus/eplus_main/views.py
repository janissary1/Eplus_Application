from django.shortcuts import render,loader
from django.http import HttpResponse


# Create your views here.


def index(request):
    # template = loader.get_template('/file_upload.html')
     return render(request, 'eplus_main/file_upload.html')