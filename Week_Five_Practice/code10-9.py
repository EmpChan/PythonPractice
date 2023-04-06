"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

var = IntVar()
but1 = Button(win, text = "button1")
but2 = Button(win, text = "button2") 
but3 = Button(win, text = "button3")

but1.pack(side = LEFT)
but2.pack(side = LEFT)
but3.pack(side = LEFT)


win.mainloop()
