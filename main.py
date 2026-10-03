from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "No text is entered in the text field")

button=Button(root, text="Routine" ,command=msg)
button.place(x=40, y=80)

root.mainloop()