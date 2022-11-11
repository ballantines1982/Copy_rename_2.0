import tkinter as tk
from tkinter import ttk
import os
import openpyxl
from openpyxl import load_workbook
import locale
import datetime
import re

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

wb = load_workbook('slask-order.xlsx')
sheet = wb['Sheet1']

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x300+700+340')
        self.title('Slask Order')
        self.attributes('-alpha', 0.9)
        self.resizable(0,0)
        options = {'padx=':10, 'pady=': 10}
        
        self.create_widgets()
      
    def create_widgets(self):
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        for i in range(3):
            self.rowconfigure(i, weight=1)
        
        optionsFrame = OptionsFrame(self)
        optionsFrame.grid(row=0, column=0, sticky=tk.NW, padx=5, pady=3)
        
        statsFrame = StatsFrame(self)
        statsFrame.grid(row=0, column=1, sticky=tk.NW, padx=5, pady=3)
        
        inputFrame = InputFrame(self)
        inputFrame.grid(row=1, column=0, sticky=tk.NW, padx=5, pady=3)
        
        levFrame = LevFrame(self)
        levFrame.grid(row=1, column=1, sticky=tk.NW, padx=5, pady=3)
        
        buttonFrame = ButtonFrame(self)
        buttonFrame.grid(row=2, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=3)
        
            
class OptionsFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        
        self.config(text='Välj Kund')
        self.slask = tk.IntVar()
        self.selected_cust = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        
        ttk.Label(self, text='Välj Kund').grid(row=0, column=0, sticky='W')
        self.cust_combo = ttk.Combobox(self, textvariable=self.selected_cust, width=20)
        self.cust_combo['values'] = ['Bravida', 'SafeTeam', 'Närhälsan', 'Folktandvården']
        self.cust_combo['state'] = 'readonly'
        self.cust_combo.grid(row=1, column=0)
        self.check_slask = ttk.Checkbutton(self, text='Slasknr?', variable=self.slask, onvalue=1, offvalue=0)
        self.check_slask.grid(row=2, column=0)
        
        for widget in self.winfo_children():
            widget.grid(sticky=tk.W, padx=5, pady=2)  
        
        
    
class StatsFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self.config(text='Stats')    
        
      
        self.create_widgets()
        

    def create_widgets(self):
        
        ttk.Label(self, text='Radvärde: \t\t').grid(row=0, column=0)
        self.radKr = ttk.Label(self, text='0.0kr')
        self.radKr.grid(row=0, column=1)
        ttk.Label(self, text='Inpris Total: \t').grid(row=3, column=0)
        self.inprisKr = ttk.Label(self, text='0.0kr')
        self.inprisKr.grid(row=3, column=1)
        ttk.Label(self, text='Marginal Total: \t').grid(row=2, column=0)
        self.margKr = ttk.Label(self, text='0.0kr')
        self.margKr.grid(row=2, column=1)
        ttk.Label(self, text='Marginal %: \t').grid(row=1, column=0)
        self.margProcent = ttk.Label(self, text='0.0%')
        self.margProcent.grid(row=1, column=1)      
        
        for widget in self.winfo_children():
            widget.grid(sticky=tk.W, padx=5)  
        
        
class InputFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
      
        
        self.config(text='Produkt Data', padx=3, pady=3)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        
        self.antalStringVar = tk.StringVar(value=0)
        self.inprisStringVar = tk.StringVar(value=0)
        self.utprisStringVar = tk.StringVar(value=0)
        self.MargProcStringVar = tk.StringVar(value=0)
        
        self.inprisStringVar.trace('w', self.calc_stuff)
        self.utprisStringVar.trace('w', self.calc_stuff)
        
        self.vcmd = (self.register(self.callback))
        
        self.create_widgets()
        
    def calc_stuff(self, *args):
        antal_raw = self.antalStringVar.get()
        antal = self.comma(antal_raw)
        inpris_raw = self.inprisStringVar.get()
        inpris = self.comma(inpris_raw)
        utpris_raw = self.utprisStringVar.get()
        utpris = self.comma(utpris_raw)
        
        self.inprisKr['text'] = str(round((inpris * antal), 2)) + 'kr\t'
        self.margKr['text'] = str(round((utpris - inpris)* antal, 2)) + 'kr\t'
        self.margProcent['text'] = str(round(((utpris-inpris)/utpris)*100, 2)) + '%\t'
        self.radKr['text'] = str(round(antal * utpris, 2)) + 'kr\t'
        
    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False   
        
        
    def comma(self, num):
        new_num = locale.atof(num)
        return new_num
        
    def create_widgets(self):
        
        self.produktStringVar = tk.StringVar()
        ttk.Label(self, text='Produkt').grid(row=0, column=0)
        self.entry_produkt = ttk.Entry(self, width=15, textvariable=self.produktStringVar)
        self.entry_produkt.grid(row=0, column=1, padx=5)
        
        
        ttk.Label(self, text='Antal').grid(row=1, column=0)
        self.entry_antal = ttk.Entry(self, width=5, textvariable=self.antalStringVar, validate='all', validatecommand=(self.vcmd, '%P'))
        self.entry_antal.grid(row=1, column=1, padx=5)
        
        ttk.Label(self, text='Inpris').grid(row=2, column=0)
        self.entry_inpris = ttk.Entry(self, width=6, textvariable=self.inprisStringVar, validate='all', validatecommand=(self.vcmd, '%P'))
        self.entry_inpris.grid(row=2, column=1, padx=5)
               
        ttk.Label(self, text='Utpris').grid(row=3, column=0)
        self.entry_utpris = ttk.Entry(self, width=6, textvariable=self.utprisStringVar, validate='all', validatecommand=(self.vcmd, '%P'))
        self.entry_utpris.grid(row=3, column=1, padx=5)
              
        for widget in self.winfo_children():
            widget.grid(sticky=tk.W, padx=5, pady=2)
        # ttk.Label(self, text='PO-nr').grid(row=0, column=4, padx=5, sticky=tk.W)
        
        # ttk.Entry(self, width=15).grid(row=1, column=4, padx=5)
              
        # ttk.Label(self, text='SO-nr').grid(row=0, column=5, padx=5, sticky=tk.W)
        # ttk.Entry(self, width=15).grid(row=1, column=5, padx=5)


class LevFrame(tk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self.selected_lev = tk.StringVar()
        self.config(text='Leverantörsinfo')
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text='Välj Leverantör').grid(row=0, column=0, sticky=tk.NW)
        self.combo_lev = ttk.Combobox(self, textvariable=self.selected_lev, width=20)
        self.combo_lev.grid(row=1, column=0, sticky=tk.NW)
        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)
        
        
class ButtonFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
            
        self.create_widgets()
        
    def create_widgets(self):

        self.btn_reset = ttk.Button(self, text='Reset')
        self.btn_reset.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        
        self.btn_ok = ttk.Button(self, text='OK', command=self.append_)
        self.btn_ok.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
    
    def append_(self):
        date_today = datetime.datetime.today()
        new_entry = [
            date_today, 
            'Kund', 
            self.entry_produkt.get(), 
            'Artnr', self.entry_antal.get(), 
            self.entry_inpris.get(), 
            self.entry_utpris.get(), 
            self.comma(self.statsFrame.margProcent['text'][:-2]), 
            self.comma(self.statsFrame.margKr['text'][:-3])]
        
        sheet.append(new_entry)
        wb.save(filename='slask-order.xlsx')


if __name__ == '__main__':
    run = Main()
    tk.mainloop()