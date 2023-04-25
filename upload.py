
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
   
import os
   
  
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
   
# mappen vi laddar upp från
path = os.getcwd() + "/files_to_upload/"   

# mappens id som vi laddar upp till
folder = "1yUN6WLTOArxmyBChM1uaiaTgh3bMZ1Vc"
 


def upload_file():
    # iterating thought all the files/folder
    # of the desired directory
    for x in os.listdir(path):        
        

        filename = os.path.join(path, x)
        files= drive.CreateFile({'parents' : [{'id' : folder}], 'title' : x})
        files.SetContentFile(filename)
        files.Upload()
        os.remove(path + x)     # tar bort filen som laddas upp
    
        # Due to a known bug in pydrive if we 
        # don't empty the variable used to
        # upload the files to Google Drive the
        # file stays open in memory and causes a
        # memory leak, therefore preventing its 
        # deletion
        files = None

