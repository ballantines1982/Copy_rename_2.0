import tkinter as tk
from tkinter import ttk
from datetime import datetime

lst = ['12.00', '15.00', '17.00']

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x600')
        
        
        
        self.root.mainloop()
    
    def create_wid(self):
        for i in range(len(lst)):
            clock = Clock(self, lst[i])
            clock.pack()
            
class Clock(tk.Frame):
    def __init__(self, container, time):
        super().__init__(container)
        self.time = time
        
        
        self.time_label = tk.Label(container, text=self.time)
        self.time_label.pack()
        
    
        
App()