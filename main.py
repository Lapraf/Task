import os
import shutil
import re
import sys

def normalize(file):
    normalize_name = file.lower()
    normalize_name = normalize_name.replace(' ', '_')
    normalize_name = re.sub(r'[^a-z0-9_.]', '_', normalize_name)
    return normalize_name

def place(file, answer, path, root_path):
    path_first = os.path.join(path, file)
    path_second = os.path.join(root_path, answer, file)
    print(file, answer, path)
    if not os.path.exists(os.path.join(root_path, answer)):
        os.makedirs(os.path.join(root_path, answer))
    if os.path.exists(os.path.join(path, answer)):
        shutil.move(path_first, path_second)



def del_dir(answer, path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(path, answer)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty folder: {dir_path}")


def define(file):
    if ".jpeg" in file or ".png" in file or ".jpg" in file or ".svg" in file or ".gif" in file:
        return "images"
    elif ".avi" in file or ".mp4" in file or ".mov" in file or ".mkv" in file or ".rec" in file:
        return "videos"
    elif ".doc" in file or ".docx" in file or ".txt" in file or ".pdf" in file or ".xlsx" in file or ".pptx" in file:
        return "documents"
    elif ".mp3" in file or ".ogg" in file or ".wav" in file or ".amr" in file:
        return "music"
    elif ".zip" in file or ".gz" in file or ".tar" in file:
        return "archives"
    else:
        return "unknown"


def sort(path):
    for address, dirs, files in os.walk(path):
        for file in files:
            # normalize(file)
            answer = define(file)
            place(file, answer, address, path)
            del_dir(answer, path)

if len(sys.argv):
    path = sys.argv[1]
    if os.path.exists(path):
        sort(path)
        print("Sorting complete.")