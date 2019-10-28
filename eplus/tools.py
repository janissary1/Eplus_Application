
#TODO: add logging information
def save_user_zip(file,username): 
    with open("User_Dirs/{}/zips/{}".format(username,file.name),"wb+") as destination:
        for data in file.chunks():
            destination.write(data)
        destination.close()