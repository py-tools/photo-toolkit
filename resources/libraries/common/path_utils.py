
import os
import glob
import shutil

def get_all_files_from_path(path, file_extension, recursive=False):
    """
    """
    if recursive:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(file_extension):
                    print(file)
    file_list = glob.glob(path)
    return file_list

def copy_files_into_folder(file_list, destination_folder):
    """
    """

    if not os.path.exists(destination_folder):
        try:
            os.mkdir(destination_folder)
        except:
            print("ERROR")
    for file in file_list:
        shutil.copy(file, destination_folder)
