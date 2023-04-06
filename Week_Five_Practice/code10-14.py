"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("400x400")

def clickL(event):
    messagebox.showinfo("mouse","You clicked image")

photo = PhotoImage(file = "img1.gif")
la = Label(win, image = photo)

la.bind("<Button-1>", clickL)

la.pack(expand = 1, anchor = CENTER)

win.mainloop()
