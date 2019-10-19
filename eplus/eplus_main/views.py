from django.shortcuts import render,loader
from django.http import HttpResponse

#kek
# Create your views here.


def index(request):
    # template = loader.get_template('/file_upload.html')
     return render(request, 'eplus_main/file_upload.html')
'''
def process_zip(request):
    #unzip files
    #return list of files with a path name/folder representing where they  are located
'''