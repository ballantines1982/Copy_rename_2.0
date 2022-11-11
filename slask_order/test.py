import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import *
from tkinter.commondialog import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x400')
        
        self.create_widgets()
        
    def create_widgets(self):
        mainFrame = MainFrame(self)
        mainFrame.grid(row=0, column=0)
        buttonFrame = ButtonFrame(self)
        buttonFrame.grid(row=1, column=0)

        
class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.lb = tk.LabelFrame(text='Items')
        self.lb.grid(row=0, column=0, sticky=tk.NW)
        
        self.test_label = ttk.Label(self.lb, text='Test')
        self.test_label.grid(row=0, column=0)
        
        
class ButtonFrame(MainFrame):
    def __init__(self, container):
        super().__init__(container)

        #self.test_label = self.test_label
        
        self.create_widgets()
    
    def create_widgets(self):
        run_btn = ttk.Button(self, text='RUN', command=self.run_app)
        run_btn.grid(row=1, column=0)
        
    def run_app(self):
        self.test_label['text'] = 'WORKED'
        
        
if __name__ == '__main__':
    run = App()
    run.mainloop()