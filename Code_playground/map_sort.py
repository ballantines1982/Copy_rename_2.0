import os
from tkinter import filedialog
from tkinter import Tk
import time
import shutil

root = Tk()
root.withdraw()

path = filedialog.askdirectory()
tStart = time.time()

images = ['.jpg', '.jpeg', '.png', '.svg']
excel = ['.xml', '.xlsx', '.xls', '.csv', '.ods']
programs = ['.exe', '.msi']
compressed = ['.zip', '.rar']
html = ['.js', '.css', '.html', '.json', '.rules']

def sortFolder(folder, list):
    dirlist = os.scandir(path)
    folder_to_create = folder 
    for file in dirlist:
        fileSplit = os.path.splitext(file)
        src_path = os.path.join(path, file)
        dest_path = os.path.join(path, folder_to_create) 
        if fileSplit[1].lower() in list:
            os.makedirs(dest_path, exist_ok=True)
            try:
                shutil.move(src_path, dest_path)
            except:
                print(f"Filen finns redan: {src_path}")
                os.remove(src_path)
    
sortFolder('Bilder', images)
sortFolder('Installations Filer', programs)
sortFolder('Excel Filer', excel)
sortFolder('Komprimerade Filer', compressed)
sortFolder('HTML Filer', html)
tEnd = time.time()

tTotal = (tEnd - tStart)
print(f'Files moved in: {tTotal:.2f} sek')
