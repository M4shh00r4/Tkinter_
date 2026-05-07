from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Message Box Window")
root.geometry("300x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text = "Scan for Virus" , command=msg)
button.place(x=80, y=100)

root.mainloop()