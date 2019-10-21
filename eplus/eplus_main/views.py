from django.shortcuts import render,loader,redirect
from django.http import HttpResponse
import time as t

#kek
# Create your views here.


def index(request):
    # template = loader.get_template('/file_upload.html')
     return render(request, 'eplus_main/file_upload.html')

def process_zip(request):
    #unzip files
    #return list of files with a path name/folder representing where they  are located
    if request.method == "POST": #request is valid
        return HttpResponse("Files uploaded: {}".format(request.FILES["zip_file"].name))

    else:
        return HttpResponse('Error invalid request', status=403)