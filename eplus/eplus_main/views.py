from django.shortcuts import render,loader,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.base import SessionBase
import multiprocessing
import tools

# Create your views here.

@login_required
def index(request):
    # template = loader.get_template('/file_upload.html')
    if request.user.is_authenticated:
        context = {"username" : request.user.username}
        print(request.session.get_expire_at_browser_close())
        return render(request, 'eplus_main/file_upload.html',context)
    else:
        return redirect(settings.LOGIN_URL_REDIRECT)

@login_required
def eplus_processes(request):
    return HttpResponse("kek")

@login_required
def process_zip(request):
    #unzip files
    if request.method == "POST": #request is valid
        #fptr = file(request.FILES["zip_file"])
        #print(request.FILES["zip_file"].name)
        file_name = request.FILES["zip_file"].name
        tools.save_user_zip(request.FILES["zip_file"],request.user.username)
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        try:
            p = multiprocessing.Process(target=tools.compile_files, args=(file_name,request.user,return_dict))
            p.start()
            #p.join()#only for testing subprocess
            print("Started compilation process for: ","PID: ",file_name,p.pid)
            #print(return_dict) #only for testing subprocess
            return redirect('submissions')
        except Exception as exc:
            return HttpResponse("Exception Occurred {}".format(exc))

    else:
        return HttpResponse('Error invalid request', status=403)