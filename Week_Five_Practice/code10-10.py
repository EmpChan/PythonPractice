"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

butL = []
for i in range(3):
    but = Button(win,text = "button"+str(i+1))
    butL.append(but)
    butL[i].pack(side = RIGHT)


win.mainloop()
