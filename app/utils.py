import zipfile
import time
import subprocess

from app import app, UPLOAD_FOLDER
import os
import glob
import zipfile

ALLOWED_EXTENSIONS = {'rar', 'tar.gz', 'png', 'jpg', 'jpeg', 'gif', 'pdf', 'zip'}
UNZIPPED_FILE_PATH = ''
FILE_NAME = ''

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

    FILE_NAME = os.path.splitext(entry[0])[0]
    UNZIPPED_FILE_PATH = UPLOAD_FOLDER + '/' + FILE_NAME
    print(UNZIPPED_FILE_PATH)



    with zipfile.ZipFile(zipped_file_path, 'r') as zip_ref:
        zip_ref.extractall(UPLOAD_FOLDER + '/')

    time.sleep(20)
    docker_file_path = ''

    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(UNZIPPED_FILE_PATH):
        for item in f:
            if 'Dockerfile' in item:
                docker_file_path = os.path.join(r, item)
                break

    print("Dockerfile path: {}".format(docker_file_path))

    lower_file_name = FILE_NAME.lower()

    subprocess.call("pwd")
    print(UNZIPPED_FILE_PATH)
    print(UNZIPPED_FILE_PATH)
    print(UNZIPPED_FILE_PATH)

    os.chdir(UNZIPPED_FILE_PATH)
    print(UNZIPPED_FILE_PATH)
    print(UNZIPPED_FILE_PATH)

    subprocess.call(["docker", "build", "-t", "myapp:latest", "."])

    print("Pushing image to portus...")
    upload_docker_image_to_portus()

    time.sleep(60)
    delete_resources()


def upload_docker_image_to_portus():
    subprocess.call(["docker", "login", "portus.hashedin.com"])
    subprocess.call(["docker", "tag", "myapp:latest", "portus.hashedin.com/sankalp.saxena/myapp:latest"])
    subprocess.call(["docker", "push", "portus.hashedin.com/sankalp.saxena/myapp:latest"])
    print("Image pushed to portus successully")


def delete_resources():
    subprocess.call(["docker", "rmi", "myapp:latest"])
    print("Image deleted successfully")