import tkinter as tk
from tkinter import ttk
import datetime
import itertools

pb = datetime.datetime(1982, 5, 18)
sb = datetime.datetime(1988, 11, 29)

birth_list = {
    "Peter": pb,
    "Sara": sb
    }

test_list = ['Peter', 'Sara', 'Alice', 'Ellen']


    
num = 0
    
class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        options = {'padx': 5, 'pady': 5}
        self.index = 0
        
        

        
        #Names
        self.number = tk.StringVar()
        self.number.set(test_list[0])
        self.l_name = ttk.Label(self, textvariable = self.number, font=('Arial', 16))
        self.l_name.grid(column=0, row=1, columnspan=2, sticky=tk.S)
        
        #Buttons
        self.prev_button = ttk.Button(self, text='Föregående', width=21, command=self.prev_date)
        self.prev_button.grid(column=0, row=2, sticky=tk.S)
        
        self.next_button = ttk.Button(self, text='Nästa', width=21, command=self.next_date)
        self.next_button.grid(column=1, row=2, sticky=tk.S)
        
        self.grid(padx=10, pady=10)

    def next_date(self):
        if not self.index >= len(test_list)-1:
            self.index+=1
            self.number.set(test_list[self.index])
        else:
            self.index = 0
            self.number.set(test_list[self.index])
        
    def prev_date(self):
        if self.index == 0:
            self.index = len(test_list)-1
            self.number.set(test_list[self.index])
        else:
            self.index-=1
            self.number.set(test_list[self.index])
            
class TopFrame(tk.Frame):
    def __init__(self, container):
        super().__init__()
        #Inscreen Title
        self.l_title = ttk.Label(self, text='Familjens Födelsedagar')
        self.l_title.grid(column=0, row=0, sticky=tk.W)
        self.l_date = ttk.Label(self, text=datetime.date.today())
        self.l_date.grid(column=1, row=0, sticky=tk.E)       
        
        self.__create_widgets()    
        
    def __create_widgets(self):
                 
            
            
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('300x150')
        self.title('Födelsedagar')
        self.attributes('-alpha', 0.9)
        
    def __create_widgets(self):
        pass
    
    
if __name__ == '__main__':
    run = Main()
    MainFrame(run)
    run.mainloop()
    

