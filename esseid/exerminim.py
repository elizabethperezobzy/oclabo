import os

folder_path = 'path_to_folder'

if not os.listdir(folder_path):
    print("Folder is empty")
else:
    print("Folder is not empty")
