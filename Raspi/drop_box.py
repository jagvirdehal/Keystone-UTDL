import dropbox
import json
from time import sleep

def download(path):
    global dbx
    dbx.files_download_to_file(path, "/data.json")
    
    data_file = open(path)
    data = json.load(data_file)

    return data

def upload(path):
    return 0


if (__name__ == "__main__"):
    dbx = dropbox.Dropbox("BqD0eu8yhmAAAAAAAAABf3vvjHH9punzxFFz_HXkz53608Vo7Ofogt0Qpx6JowGK")
    while True:
        upload("data_upload.json")
        download("data_download.json")
        sleep(3)
else:
    dbx = dropbox.Dropbox("BqD0eu8yhmAAAAAAAAABf3vvjHH9punzxFFz_HXkz53608Vo7Ofogt0Qpx6JowGK")
    download("data_download.json")
    download("data_upload.json")
