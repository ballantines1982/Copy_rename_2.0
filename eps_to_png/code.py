from PIL import Image
import os
from tkinter.filedialog import askdirectory, askopenfilename
import tkinter as tk
from tkinter import ttk

pathStr = ''
fileCounter = 0

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x200')
        self.title('EPS to PNG')
        
        self.__create_wid()
        
    def __create_wid(self):
        leftFrame = LeftFrame(self)
        leftFrame.grid(row=0, column=0, sticky=tk.NW)
        
        rightFrame = RightFrame(self)
        rightFrame.grid(row=0, column=1, sticky=tk.NE)
        bottomFrame = BottomFrame(self)
        bottomFrame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=3, padx=3)
        
        

class BottomFrame(ttk.Frame):
    global path, folderInfo
    path = ''
    folderInfo = ''
    
    def __init__(self, container):
        super().__init__(container)
        global path
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.fileCounter = 0
        self.varPath = tk.StringVar()
        tk.Label(self, text='Folder/Fil:').grid(row=0, column=0, sticky=tk.W)
        path = tk.Label(self, text='', textvariable=path)
        path.grid(row=1, column=0, sticky=tk.NW)
        folderInfo = tk.Label(self, text='')
        folderInfo.grid(row=2, column=0, sticky=tk.NW)
        btnConvert = tk.Button(self, text='Konvertera', command=self.convert)
        btnConvert.grid(row=3, column=1, sticky=tk.E)
        


        
    def convert(self):
        files = os.listdir()
        counter = 0
        
        for file in files:
            if file.endswith('.eps'):
                epsFile = Image.open(file)
                try:
                    rgbEpsFile = epsFile.convert('RGBA')
                except OSError:
                    print('OSError')
                pngFile = file[:-4] + '.png'
                try:
                    rgbEpsFile.save(pngFile, bitmap_format='png')
                    counter+=1
                    print('Converting images..')
                except:
                    print('Error while saving..')
        
        print(f'{counter} .png files created')



class LeftFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.lbfMapp = tk.LabelFrame(self, text='Välj hel Mapp')
        self.lbfMapp.grid(row=0, column=0, padx=3, pady=5)
        
        self.__create_wid()
        
    def __create_wid(self):
        tk.Label(self.lbfMapp, text='Test').grid(row=0, column=0, sticky=tk.NW)
        btnMapp = tk.Button(self.lbfMapp, text='Välj Mapp', command=self.epsToPngMapp, width=13)
        btnMapp.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
        

    def epsToPngMapp(self):
        #global fileCounter, folderInfo
        askDir = askdirectory()
        os.chdir(askDir)
        self.cwd = os.getcwd()
        path.config(text = self.cwd)
        dirFiles = os.listdir(self.cwd)
        fileCounter = 0
        for file in dirFiles:
            if file.endswith('.eps'):
                fileCounter+=1
        BottomFrame.folderInfo.config(text=str(fileCounter) + ' files in selected folder')
        fileCounter = 0
        
        
                
        
        


class RightFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.lbfFil = tk.LabelFrame(self, text='Välj enstaka fil')
        self.lbfFil.grid(row=0, column=0, padx=3, pady=5)
        self.__create_wid()
        
    def __create_wid(self):
        tk.Label(self.lbfFil, text='Test').grid(row=0, column=0, sticky=tk.NW)
        btnFil = tk.Button(self.lbfFil, text='Välj Fil', command=self.epsToPngFil, width=13)
        btnFil.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
        
    def epsToPngFil(self):
        askFile = askopenfilename(initialdir='/', title='Välj fil',  filetypes=(("eps files", "*.eps"), ("all files", "*.*")))
        epsFile = Image.open(askFile)
        pngFile = askFile[:-4] + '.png'
        try:
            rgbEpsFile = epsFile.convert('RGBA')
        except OSError:
            print('OSError')
        try:
            rgbEpsFile.save(pngFile, bitmap_format='png')
        except:
            print('Error while saving..')
        
        print(f'{pngFile} created')
        
        

if __name__ == '__main__':
    run = App()
    run.mainloop()
    
    

"""
Konvertera knappen skall känna av om man valt FIL eller MAPP, kanske genom variabeln pathStr.get() och sen en if sats med endswith()
if path.endswith('\'):
    run MAPP func
else:
    run FIL func
    
    
Funktion som märker av att man valt Mapp eller FIl och sen tar action ut efter det.

Funtionerna MAPP & FIL måste returna den valda pathen 

IDÉ: En global variabel som känner av det senaste valet av MAPP & FIL, säg att den initieras med 0, Mapp sätter variabeln som 1 och FIL som 2.
    Konvertera kanppen kör functionerna ut efter det.

"""