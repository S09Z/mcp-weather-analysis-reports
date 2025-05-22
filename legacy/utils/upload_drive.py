from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def upload_to_drive(filepath):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # ใช้ครั้งแรกต้องเปิด browser เพื่อ auth

    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': os.path.basename(filepath)})
    file.SetContentFile(filepath)
    file.Upload()
    return file['alternateLink']