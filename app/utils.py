import zipfile
from app import app, UPLOAD_FOLDER
import os
import glob
import zipfile

ALLOWED_EXTENSIONS = {'rar', 'tar.gz', 'png', 'jpg', 'jpeg', 'gif', 'pdf', 'zip'}
UNZIPPED_FILE_PATH = ''


def allowed_file(filetype):
    print(filetype, 'filename')
    for allowed_ext in ALLOWED_EXTENSIONS:
        if allowed_ext in filetype.lower():
            return True
    return False

def unzip_folder():
    entry = os.listdir(UPLOAD_FOLDER)
    print(UPLOAD_FOLDER)
    print(entry)
    zipped_file_path = UPLOAD_FOLDER + '/' + entry[0]
    print(zipped_file_path)
    UNZIPPED_FILE_PATH = UPLOAD_FOLDER + '/' + os.path.splitext(entry[0])[0]
    print(UNZIPPED_FILE_PATH)

    with zipfile.ZipFile(zipped_file_path, 'r') as zip_ref:
        zip_ref.extractall(UPLOAD_FOLDER + '/')

def get_dockerfile():
    print("inside te ")

    '''
    pys = []
    for p, d, f in os.walk(UNZIPPED_FILE_PATH):
        for file in f:
            print(file)
            if file.endswith('Dockerfile'):
                pys.append(file)
    print(pys)
    
    '''