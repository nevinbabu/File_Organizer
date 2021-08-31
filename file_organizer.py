import os, shutil
from pathlib import Path

#Dictionary of folders with corresponding exrensions
DIR = {
    "Docs": [".pdf", ".xls", ".xlsx", ".doc", ".docx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Audio": [".mp3", ".wav"],
    "Software": [".exe"]
}

#Function to find the folder for corresponding file extension
def find_dir(ext):
    for category, extensions in DIR.items():
        for extension in extensions:
            if extension == ext:
                return category
    return "Others"


#Function to move the files to corresponding folders
def organize(path):
    os.chdir(path)
    items = os.scandir(path)
    for item in items:
        if os.path.isdir(item):
            continue
        file_path = Path(item)
        ext = file_path.suffix.lower()
        dir = find_dir(ext)
        dir_path = Path(dir)
        if dir_path.is_dir() != True:
            dir_path.mkdir()
        shutil.move(str(file_path), dir_path)


#To enter the path of directory to be organized
#Eg:If you need to organize Downloads input should be: C:\\Users\\username\\Downloads
path = input("Enter path: ")
organize(path)