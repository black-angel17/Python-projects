


#file moving of the screenshot to trash folder

#put to trash if .png is detected
import os
from pathlib import Path
import shutil
import time

src_folder = r"C:\Users\ADMIN\Documents\Greenshot"

dest = r"C:\Users\ADMIN\Documents\Greenshot\Trash"

def move(src, dst):
    shutil.move(src, dst)

def is_png(file_path):
    file_extension = Path(file_path).suffix
    return file_extension.lower() == ".png"

while True:

    for name in os.listdir(src_folder):
        file_path = os.path.join(src_folder, name)

        if is_png(file_path):
            time.sleep(60)
            move(file_path, dest)
            print("this is png --  i moved it ")
        else:
            continue
    # return as a list on x
