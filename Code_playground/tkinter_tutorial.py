import tkinter as tk
from tkinter.filedialog import askdirectory


def change_text():
    if lbl_welcome["text"] == "Welcome":
        lbl_welcome["text"] = "UNNA SIG"
        lbl_welcome["fg"] = "green"
    else:
        lbl_welcome["text"] = "Welcome"
        lbl_welcome["fg"] = "black"

def askdir():
    folder = askdirectory("Select folder")

window = tk.Tk()

window.title("UNNA SIG")

frm_welcome = tk.Frame(master=window)
lbl_welcome = tk.Label(
    text="Welcome",
    master=frm_welcome,
    width=15, 
    pady=5
    )
lbl_welcome.pack()

frm_btn_click = tk.Frame(master=window)
btn_click = tk.Button(
    text="Click me!",
    master=frm_btn_click,
    command=change_text,
    pady=5
    )
btn_click.pack()

frm_btn_select_dir = tk.Frame(master=window)
btn_select_dir = tk.Button(
    text="Select Folder",
    master=frm_btn_click,
    command=askdir,
    pady=5
    )
frm_btn_select_dir.pack()

frm_welcome.grid(row=0, column=0, pady=10, padx=10)
frm_btn_click.grid(row=0, column=1, pady=10, padx=10)
frm_btn_select_dir.grid(row=1, column=1, pady=10, padx=10)
window.mainloop()