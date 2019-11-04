import zipfile
import datetime

#TODO: add logging information
def save_user_zip(file,username): 
    with open("User_Dirs/{}/zips/{}".format(username,file.name),"wb+") as destination:
        for data in file.chunks():
            destination.write(data)
        destination.close()

def compile_files(file_name,username):
    with zipfile.ZipFile("User_Dirs/{}/zips/{}".format(username,file_name),"r") as input_archive:
        date = datetime.datetime.now().strftime("%b-%d-%H-%M")
        input_archive.extractall("User_Dirs/{}/idf_outputs/{}-{}".format(username,file_name,date))

    #move zip file to idf_outputs
    #unzip file
    #run eplus on each .idf, make a new folder for outputs
    #