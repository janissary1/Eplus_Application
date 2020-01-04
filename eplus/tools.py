import zipfile
import datetime
import subprocess
import os
import shutil

from django.db import models
from eplus_main.models import Process

#TODO: add logging information
def save_user_zip(file,username): 
    with open("User_Dirs/{}/zips/{}".format(username,file.name),"wb+") as destination:
        for data in file.chunks():
            destination.write(data)
        destination.close()
#add cpu core setting
def compile_files(file_name,user,output_dict):
    p_id = os.getpid()
    with zipfile.ZipFile("User_Dirs/{}/zips/{}".format(user.username,file_name),"r") as input_archive:
        date = datetime.datetime.now().strftime("%b-%d-%H-%M")
        file_root = file_name[:file_name.find(".")]
        upload_path = "User_Dirs/{}/idf_outputs/{}-{}".format(user.username,file_root,date) #specifies the location of the User's file
        input_archive.extractall(upload_path)
        
        files = os.listdir(upload_path + "/" + file_root) #ZIP file must have same name as zipped folder within (file_root)
        
        file_path = os.getcwd() + "/{}/{}".format(upload_path,file_root)
        
        args = ['resources/EnergyPlus-8-9-0/energyplus.exe','{}/{}'.format(file_path,files[0])]
        
        #output_dict['Data'] = str(files[0])

        p_record = Process(username=user,pid=p_id,current_file=1,total_files=len(files),errors=0)
        p_record.save()

        paths = []
        codes = []
        for idf in files:
            if idf != "__MACOSX":
                file_name = idf[:idf.find(".")]
                output_dir = upload_path + "/" + file_root + "/" + file_name
                os.mkdir(output_dir) #each idf file creates multiple files on processing, so a dir is required
                p_record = Process.objects.get(username=user.username, pid=p_id) #get the record of this process
                output_dict['Paths'] = paths#
                shutil.copyfile('resources/mtr.rvi',output_dir + "/mtr.rvi")

                subprocess.call(["resources/EnergyPlus-8-9-0/energyplus","-w","resources/TorontoWeather.epw","-r","-d",output_dir,"{}/{}".format(file_path,idf)])
                p_record.current_file = models.F('current_file') + 1
                p_record.save()
        output_dict['Paths'] = paths
        output_dict['Codes'] = codes

        #figure out if no issues when two people compiling
        #add error checking if file has already been uploaded for a given user
        
