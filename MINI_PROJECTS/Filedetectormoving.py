from pathlib import Path
import os

import shutil

"""
password ==0002323

"""
destination_folder = r'C:\Users\ADMIN\Videos'

def move(src, dst):
    shutil.move(src, dst)

def is_mp4_file(file_path):
    file_extension = Path(file_path).suffix
    return file_extension.lower() == ".mp4"


# to loop the total files on folder


folder_path = r"C:\Users\ADMIN\PycharmProjects\pythonProject\#directory_path#"  # Specify the folder path

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Perform actions on each file
    print("File:", file_name)
    print("Full Path:", file_path)
    if is_mp4_file(file_path):
        move(file_path,destination_folder)
        print("------moved------")
    else:
        print("File is not an MP4 video.")

    # Add your desired code here to process each file
    # For example, you can check if it's an MP4 file using the previously provided function is_mp4_file(file_path)
    # or perform any other operations on the file
