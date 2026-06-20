from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showinfo("Alert", "Stop! Virus Found.")

button = Button(root, text= "Scan for Virus", command = msg)
button.pack()
root.mainloop()