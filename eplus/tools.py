import zipfile
import datetime
import subprocess

#TODO: add logging information
def save_user_zip(file,username): 
    with open("User_Dirs/{}/zips/{}".format(username,file.name),"wb+") as destination:
        for data in file.chunks():
            destination.write(data)
        destination.close()

def compile_files(file_name,username):
    with zipfile.ZipFile("User_Dirs/{}/zips/{}".format(username,file_name),"r") as input_archive:
        date = datetime.datetime.now().strftime("%b-%d-%H-%M")
        file_root = file_name[:file_name.find(".")]
        input_archive.extractall("User_Dirs/{}/idf_outputs/{}-{}.zip".format(username,file_root,date))

    #move zip file to idf_outputs
    #unzip file
    #run eplus on each .idf, make a new folder for outputs
    #