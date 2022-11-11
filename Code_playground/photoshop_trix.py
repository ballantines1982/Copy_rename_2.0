import win32com.client
import os
from tkinter.filedialog import askdirectory, askopenfile

#ask_source_dir = askdirectory("Choose source folder")

psApp = win32com.client.Dispatch("Photoshop.Application")


