import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from functions import generate, labelVisibility, on_entry_click, on_focus_out, ROOT_DIR
from helper import myLower


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        messagebox.showinfo("Açıklama", self.text)

    def leave(self, event=None):
        pass

def startGui():
    global gui
    gui = tk.Tk()
    gui.title("Password Generator For Hackers")
    ico = Image.open(f'{ROOT_DIR}\\hacker.png')
    photo = ImageTk.PhotoImage(ico)
    gui.wm_iconphoto(False, photo)
    gui.configure(background='black')

    global width , height, entry_additionalName, placeholder

    placeholder = "For Wifi Wordlist.."
    
    width= 400
    height= 280

    gui.geometry("{}x{}".format(width, height))
    gui.eval('tk::PlaceWindow . center')

    frame = Frame(gui, bg="black")
    frame.pack()

    label_domain = Label(frame, text='Domain :', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2)
    entry_domain = Entry(frame, fg='green', bg="black", bd=0, highlightthickness=1, highlightbackground="#4b4646", insertbackground='green', font=('Calibri',11, 'bold'), justify="center")
    label_domain.grid(row=0,column=0, pady=5, sticky="w")
    entry_domain.grid(row=0,column=1, pady=15, sticky="w")

    label_year_of_establishment = Label(frame, text='Year of establishment :', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2)
    entry_year_of_establishment = Entry(frame, fg='green', bg="black", bd=0, highlightthickness=1, highlightbackground="#4b4646", insertbackground='green', font=('Calibri',11, 'bold'), justify="center")
    label_year_of_establishment.grid(row=1,column=0, pady=5, sticky="w")
    entry_year_of_establishment.grid(row=1,column=1, pady=15, sticky="w")

    label_username = Label(frame, text='Username :', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2)
    entry_username= Entry(frame, fg='green', bg="black", bd=0, highlightthickness=1, highlightbackground="#4b4646", insertbackground='green', font=('Calibri',11, 'bold'), justify="center")
    label_username.grid(row=2,column=0, sticky="w")
    entry_username.grid(row=2,column=1, sticky="w")

    label_surname = Label(frame, text='Surname :', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2)
    entry_surname= Entry(frame, fg='green', bg="black", bd=0, highlightthickness=1, highlightbackground="#4b4646", insertbackground='green', font=('Calibri',11, 'bold'), justify="center")
    label_surname.grid(row=3,column=0, sticky="w")
    entry_surname.grid(row=3,column=1, sticky="w")

    label_additionalName = Label(frame, text='Additional Names :', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2)
    entry_additionalName= Entry(frame, fg='green', bg="black", bd=0, highlightthickness=1, highlightbackground="#4b4646", insertbackground='green', font=('Calibri',11, 'bold'), justify="center")
    entry_additionalName.insert(0, placeholder)
    entry_additionalName.config(fg="#343333")
    tooltip = Tooltip(label_additionalName, "Enter words separated by commas. (domain1,domain2 etc.)")
    entry_additionalName.bind("<FocusIn>", on_entry_click)
    entry_additionalName.bind("<FocusOut>", on_focus_out)    
    #label_additionalName.grid(row=4,column=0, sticky="w")
    #entry_additionalName.grid(row=4,column=1, sticky="w")

    checkbox_passPol = IntVar()
    checkBox_hard= Checkbutton(frame, text='Password Policy Enabled', fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2, variable=checkbox_passPol)
    checkBox_hard.grid(row=5,column=1, sticky="w", columnspan=1)

    checkbox_wifiVar = IntVar()
    checkBox_wifi= Checkbutton(frame, text='Wifi (In Progress)', fg='green', bg='black', font=('Calibri',12, 'bold'), state="disabled", highlightcolor="green", highlightbackground="green", bd=2, variable=checkbox_wifiVar, command=lambda : labelVisibility(checkbox_wifiVar.get(), label_additionalName, entry_additionalName))
    checkBox_wifi.grid(row=6,column=1, sticky="w", columnspan=1)

    button_generate = Button(frame, text='Generate',fg='green', bg='black', font=('Calibri',12, 'bold'), highlightcolor="green", highlightbackground="green", bd=2, command=lambda domainName=entry_domain, year=entry_year_of_establishment, passPol=checkbox_passPol, name=entry_username,surname=entry_surname, wifiPol=checkbox_wifiVar: generate(myLower(domainName.get().strip()), year.get(), name.get().strip(), surname.get().strip(), passPol.get(), wifiPol.get()))
    button_generate.grid(row=8,column=1, sticky="e")

    gui.mainloop()


