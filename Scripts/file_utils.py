import os
import shutil

def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        file_info = {
            'name': filename,
            'size': os.path.getsize(path),
            'modified': os.path.getmtime(path),
            'type': 'Folder' if os.path.isdir(path) else 'File',
        }
        files.append(file_info)
    return files

def move_file(src, dst):
    shutil.move(src, dst)

def delete_file(path):
    os.remove(path)
