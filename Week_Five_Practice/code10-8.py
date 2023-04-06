"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

def myfunc():
    if var.get() == 1:
        la1.configure(text = "Python")
    elif var.get()==2:
        la1.configure(text = "C++")
    else:
        la1.configure(text = "Java")
        
win = Tk()

var = IntVar()
rb1 = Radiobutton(win, text = "Python", variable = var, value = 1, command = myfunc)
rb2 = Radiobutton(win, text = "C++", variable = var, value = 2, command = myfunc) 
rb3 = Radiobutton(win, text = "Java", variable = var, value = 3, command = myfunc)
la1 = Label(win,text = " 선택한 언어 ", fg = "violet")

rb1.pack()
rb2.pack()
rb3.pack()
la1.pack()

win.mainloop()
