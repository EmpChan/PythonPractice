"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

def click(event):
    messagebox.showinfo("click","You clicked")

win.bind("<Button>", click)

win.mainloop()
