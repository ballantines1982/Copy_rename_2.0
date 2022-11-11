import tkinter as tk
from time import strftime
import datetime
import os

window = tk.Tk()
window.title("Datum")

date_list = [[2021,9,15,2,0,0], [2022,5,18,0,0,0]]

        
    
lst = []
def read_file():
    with open('dates.txt') as file:
        for index, line in enumerate(file):
            lst.append(line.strip())
        return lst
read_file()

for line in lst:
    y = datetime.datetime(line)
    x = tk.Label(textvariable=line)
    if y < datetime.datetime.now():
        line.set(datetime.datetime.now() - y)
    line.set(y - datetime.datetime.now())
    x.pack()




# def time_test():
    
    
#     now = datetime.datetime.now()
#     nyk_start = datetime.datetime(2021,9,15,2,0,0)
#     ps_birthday = datetime.datetime(2022,5,18,0,0,0)

#     nyk_diff = now - nyk_start
#     ps_birthday_diff = ps_birthday - now

#     lbl_nykter.config(text=nyk_diff)
#     lbl_nykter.after(25, time_test)
#     lbl_ps_birthday.config(text=ps_birthday_diff)

#     # print(diff, end='')
#     # print('\b' * len(diff), end='',flush=True)

# lbl_nykter = tk.Label(window)
# lbl_nykter.pack()
# lbl_ps_birthday = tk.Label(window)
# lbl_ps_birthday.pack()

# read_file()
# time_test()
window.mainloop()