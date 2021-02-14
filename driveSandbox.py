from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime, date
today_date = date.today().strftime('%m-%d-%y')

# authenticate Google Drive user and save credentials to file
def google_drive_authentication():
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
def create_new_daily_folder(GoogleDriveObject):
    file_metadata = {'title': f'''{today_date} CHARTS''',
                     'parents': [{'id': '1htYh7OIGirRpNxFvZIOD5TTwBqvsBxw9',
                                  'kind': 'drive#childList'}],
                     'mimeType': 'application/vnd.google-apps.folder'}
    folder = GoogleDriveObject.CreateFile(file_metadata)
    folder.Upload()
    return folder['id']

#upload file from computer to GoogleAPI
def chart_file_upload(GoogleDriveObject, parentFolderKey, filePath):
    file_metadata = {'title': f'''{today_date} CHART FILE.pdf''',
                     'parents': [{'id': parentFolderKey,
                                  'kind': 'drive#childList'}]}
    file = GoogleDriveObject.CreateFile(file_metadata)
    file.SetContentFile(filePath)
    file.Upload()

#get current working directory
path = os.getcwd()
print(path)

# get folder name and id
folder_list = drive.ListFile({'q': 'trashed=false'}).GetList()
for folder in folder_list:
    print ('folder title: %s, id: %s' % (folder['title'], folder['id']))


#creates google drive object, new folder dated for today, uploads file from cpu
drive = google_drive_authentication()
daily_folder_id = create_new_daily_folder(drive)
chart_file_upload(drive, daily_folder_id)
