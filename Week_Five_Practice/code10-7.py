"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

def myfunc():
    if chk.get() == 1:
        messagebox.showinfo("","Check button is checked")
    else:
        messagebox.showinfo("","Check button is unchecked")

win = Tk()

chk = IntVar()
cbut = Checkbutton(win, text = "Click Me",variable = chk\
                   , command = myfunc)

cbut.pack()

win.mainloop()
