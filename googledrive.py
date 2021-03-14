from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime, date

# authenticate Google Drive user and save credentials to file
def gdrive_authentication():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    return drive

#create daily folder on Google Drive
def gdrive_new_daily_folder(GoogleDriveObject):
    file_metadata = {'title': f'''{today_date} CHARTS''',
                     'parents': [{'id': '1htYh7OIGirRpNxFvZIOD5TTwBqvsBxw9',
                                  'kind': 'drive#childList'}],
                     'mimeType': 'application/vnd.google-apps.folder'}
    folder = GoogleDriveObject.CreateFile(file_metadata)
    folder.Upload()
    return folder['id']

def gdrive_file_upload(GoogleDriveObject, parentFolderKey, filePath, fileTitle):
    file_metadata = {'title': fileTitle,
                     'parents': [{'id': parentFolderKey,
                                  'kind': 'drive#childList'}]}
    file = GoogleDriveObject.CreateFile(file_metadata)
    file.SetContentFile(filePath)
    file.Upload()
