from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # ต้อง auth ครั้งแรก
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)
f = drive.CreateFile({'title': "myfile.png"})
f.SetContentFile("path/to/myfile.png")
f.Upload()
print("Uploaded to:", f['alternateLink'])
