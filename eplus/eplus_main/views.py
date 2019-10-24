from django.shortcuts import render,loader,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # template = loader.get_template('/file_upload.html')
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, 'eplus_main/file_upload.html')
    else:
        return redirect(settings.LOGIN_URL_REDIRECT)

@login_required
def process_zip(request):
    #unzip files
    #return list of files with a path name/folder representing where they  are located
    if request.method == "POST": #request is valid
        fptr = file(request.FILES["zip_file"])
        fptr = open
        return HttpResponse("Files uploaded: {}".format(request.FILES["zip_file"].name))

    else:
        return HttpResponse('Error invalid request', status=403)