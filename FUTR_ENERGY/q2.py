import gdown
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def download_file(file_id, output_folder):
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output_folder, quiet=False)

def download_folder(drive, folder_id, output_path):
    folder = drive.CreateFile({'id': folder_id})
    folder.FetchMetadata()
    
    output_folder = os.path.join(output_path, folder['title'])
    os.makedirs(output_folder, exist_ok=True)

    for file in drive.ListFile({'q': f"'{folder_id}' in parents"}).GetList():
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            download_folder(drive, file['id'], output_folder)
        else:
            download_file(file['id'], output_folder)

def download_google_drive_folder(folder_link, output_path='.'):
    drive = authenticate_drive()

    # Extract folder ID from the Google Drive link
    folder_id = folder_link.split("/")[-1]

    # Download the entire folder
    download_folder(drive, folder_id, output_path)

    print(f"Folder downloaded to: {output_path}")

# Example usage
google_drive_link = "https://drive.google.com/drive/folders/1_C7I2658qnRP54gw1igYCXoyWGb8p_9h"
download_google_drive_folder(google_drive_link)
