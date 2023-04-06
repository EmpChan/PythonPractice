"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

def myfunc():
    messagebox.showinfo("Humor button","Is that funny?")

win = Tk()

photo = PhotoImage(file = "img1.gif")
but = Button(win, image = photo, command = myfunc)

but.pack()

win.mainloop()
