import tkinter as tk
from tkinter import Label, ttk
import os
from tkinter.constants import RIGHT
from openpyxl import *

from openpyxl import load_workbook
import locale
import datetime


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

wb = load_workbook('slask-order.xlsx')
sheet = wb['Sheet1']

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('470x275+700+340')
        self.title('Slask Order')
        self.attributes('-alpha', 0.9)
        self.resizable(0,0)

        
        self.create_widgets()
      
    def create_widgets(self):
        
        optionsFrame = MainFrame(self)
        optionsFrame.pack(fill='both', expand=True)
        

        
        
        
            
class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        
        self.create_widgets()

    def create_widgets(self):
        options = {'padx': 5, 'pady': 5}
        
        self.slask = tk.IntVar()
        self.selected_cust = tk.StringVar()
        
        self.lf_customer = tk.LabelFrame(self, text='Välj Kund', height=50)
        self.lf_customer.grid(row=0, column=0, sticky=tk.NSEW, **options)
        self.cust_combo = ttk.Combobox(self.lf_customer, textvariable=self.selected_cust)
        self.cust_combo['values'] = ['Bravida', 'SafeTeam', 'Närhälsan', 'Folktandvården']
        self.cust_combo['state'] = 'readonly'
        self.cust_combo.grid(row=1, column=0, padx=5, pady=8)
        self.check_slask = ttk.Checkbutton(self.lf_customer, text='Slasknr?', variable=self.slask, onvalue=1, offvalue=0)
        self.check_slask.grid(row=2, column=0, sticky=tk.W, **options)
        
        #############################################################################
        
        self.lf_stats = tk.LabelFrame(self, text='Stats')
        self.lf_stats.grid(row=0, column=1, sticky='we', columnspan=2, **options)
        self.lf_stats.columnconfigure(0, weight=1)
        self.lf_stats.columnconfigure(1, weight=1)
        ttk.Label(self.lf_stats, text='Radvärde:', width=25).grid(row=0, column=0, sticky=tk.EW)
        self.radKr = ttk.Label(self.lf_stats, text='0.0kr', anchor='e', width=15, justify=RIGHT)
        self.radKr.grid(row=0, column=1, sticky='e')
        ttk.Label(self.lf_stats, text='Inpris Total:').grid(row=3, column=0)
        self.inprisKr = ttk.Label(self.lf_stats, text='0.0kr', anchor='e', width=15, justify=RIGHT)
        self.inprisKr.grid(row=3, column=1, sticky='e')
        ttk.Label(self.lf_stats, text='Marginal Total:').grid(row=2, column=0)
        self.margKr = ttk.Label(self.lf_stats, text='0.0kr', anchor='e', width=15, justify=RIGHT)
        self.margKr.grid(row=2, column=1, sticky='e')
        ttk.Label(self.lf_stats, text='Marginal %:').grid(row=1, column=0)
        self.margProcent = ttk.Label(self.lf_stats, text='0.0%', anchor='e', width=15, justify=RIGHT)
        self.margProcent.grid(row=1, column=1, sticky='e')      
        
        for wid in self.lf_stats.winfo_children():
            wid.grid(sticky=tk.W)
                
        
        #############################################################################
    
        self.produktStringVar = tk.StringVar()
        self.antalStringVar = tk.StringVar(value=0)
        self.inprisStringVar = tk.StringVar(value=0)
        self.utprisStringVar = tk.StringVar(value=0)
        self.MargProcStringVar = tk.StringVar(value=0)
        self.inprisStringVar.trace('w', self.calc_stuff)
        self.utprisStringVar.trace('w', self.calc_stuff)
        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        vcmdAntal = (self.register(self.onValidateAntal),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.lf_produkt = tk.LabelFrame(self, text='Produkt Info')
        self.lf_produkt.grid(row=1, column=0, sticky=tk.NW, **options)
        ttk.Label(self.lf_produkt, text='Produkt').grid(row=0, column=0)
        self.entry_produkt = ttk.Entry(self.lf_produkt, width=15, textvariable=self.produktStringVar)
        self.entry_produkt.grid(row=0, column=1, padx=5)
        
        ttk.Label(self.lf_produkt, text='Antal').grid(row=1, column=0)
        self.entry_antal = ttk.Entry(self.lf_produkt, width=5, textvariable=self.antalStringVar, validate="key", validatecommand=vcmdAntal)
        self.entry_antal.grid(row=1, column=1, padx=5)
        
        ttk.Label(self.lf_produkt, text='Inpris').grid(row=2, column=0)
        self.entry_inpris = ttk.Entry(self.lf_produkt, width=6, textvariable=self.inprisStringVar, validate='key', validatecommand=vcmd)
        self.entry_inpris.grid(row=2, column=1, padx=5)
               
        ttk.Label(self.lf_produkt, text='Utpris').grid(row=3, column=0)
        self.entry_utpris = ttk.Entry(self.lf_produkt, width=6, textvariable=self.utprisStringVar, validate='key', validatecommand=vcmd)
        self.entry_utpris.grid(row=3, column=1, padx=5)
        
        for wid in self.lf_produkt.winfo_children():
            wid.grid(sticky=tk.W, pady=2)
        
        #############################################################################        
            
        self.selected_lev = tk.StringVar()
        self.levArtNrStringVar = tk.StringVar()
        
        self.lf_lev = tk.LabelFrame(self, text='Leverantörs Info')
        self.lf_lev.grid(row=1, column=1, sticky=tk.NSEW, **options)                
        ttk.Label(self.lf_lev, text='Välj Leverantör').grid(row=0, column=0, sticky=tk.NW, padx=5)
        self.combo_lev = ttk.Combobox(self.lf_lev, textvariable=self.selected_lev, width=20)
        self.combo_lev.grid(row=1, column=0, sticky=tk.NW, pady=3, padx=5)
        ttk.Label(self.lf_lev, text='Lev.Art.Nr').grid(row=2, column=0, sticky=tk.NW, padx=5)
        self.entry_levArtNr = ttk.Entry(self.lf_lev, width=15, textvariable=self.levArtNrStringVar)
        self.entry_levArtNr.grid(row=3, column=0, sticky=tk.NW, pady=3, padx=5)
        
        ############################################################################# 
        self.purchNrStringVar = tk.StringVar()
        self.orderNrStringVar = tk.StringVar()
        
        self.lf_order = tk.LabelFrame(self, text='Order Info')
        self.lf_order.grid(row=1, column=2, sticky=tk.NSEW, **options)
        ttk.Label(self.lf_order, text='Ordernummer').grid(row=0, column=0)
        self.entry_ordernr = ttk.Entry(self.lf_order, width=15, textvariable=self.orderNrStringVar, validate="key", validatecommand=vcmdAntal)
        self.entry_ordernr.grid(row=1, column=0)
        ttk.Label(self.lf_order, text='Inköpsnummer').grid(row=2, column=0)
        self.entry_purchnr = ttk.Entry(self.lf_order, width=15, textvariable=self.purchNrStringVar, validate="key", validatecommand=vcmdAntal)
        self.entry_purchnr.grid(row=3, column=0)
        
        for wid in self.lf_order.winfo_children():
            wid.grid(padx=5, sticky=tk.W)
            print(wid.winfo_class())
            if wid.winfo_class() == 'TEntry':
                wid.grid(pady=3)

        
        ############################################################################# 
        self.btn_reset = ttk.Button(self, text='Reset')
        self.btn_reset.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
        
        self.btn_ok = ttk.Button(self, text='OK', command=self.append_)
        self.btn_ok.grid(row=2, column=2, padx=5,pady=5, sticky=tk.W)
        
    def read_cust_file(self):
        cust_list = []

        f = open('cust_data.txt', 'w')
        for line in f:
            cust_list.append()
            
                
        
    
    def append_(self):
        date_today = datetime.datetime.today()
        new_entry = [
            date_today, 
            self.selected_cust.get(), 
            self.entry_produkt.get(), 
            'SAP artnr',
            int(self.entry_antal.get()), 
            float(self.entry_inpris.get()), 
            float(self.entry_utpris.get()), 
            float(self.comma(self.margProcent['text'][:-2])), 
            float(self.comma(self.margKr['text'][:-3])),
            'Levnr',
            self.selected_lev.get(),
            self.levArtNrStringVar.get(),
            int(self.orderNrStringVar.get()),
            int(self.purchNrStringVar.get())]
        
        sheet.append(new_entry)
        
        # colH = sheet['H']
        # colH.style = 'Percent'
        # colFG = sheet['F:G']
        # colFG.style = 'Currency'

            
        wb.save(filename='slask-order.xlsx')
        
        
    def calc_stuff(self, *args):
        antal_raw = self.antalStringVar.get()
        antal = self.comma(antal_raw)
        inpris_raw = self.inprisStringVar.get()
        inpris = self.comma(inpris_raw)
        utpris_raw = self.utprisStringVar.get()
        utpris = self.comma(utpris_raw)
        
        self.inprisKr['text'] = str(round((inpris * antal), 2)) + 'kr'
        self.margKr['text'] = str(round((utpris - inpris)* antal, 2)) + 'kr'
        self.margProcent['text'] = str(round(((utpris-inpris)/utpris)*100, 2)) + '%'
        self.radKr['text'] = str(round(antal * utpris, 2)) + 'kr'
        
        
    def onValidate(self, d, i, P, s, S, v, V, W):
        if S == ',' or str.isdigit(S) or S == "":
            return True
        else:
            self.bell()
            return False
    
    def onValidateAntal(self, d, i, P, s, S, v, V, W):
        if str.isdigit(S) or S == "":
            return True
        else:
            self.bell()
            return False
        
             
    def comma(self, num):
        new_num = locale.atof(num)
        return new_num
    

if __name__ == '__main__':
    run = Main()
    tk.mainloop()
    