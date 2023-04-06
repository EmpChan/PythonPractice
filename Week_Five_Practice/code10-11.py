"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

butL = []
for i in range(9):
    f = "img"+str(i+1)+".gif"
    photo = PhotoImage(file = f)
    but = Button(win,image = photo)
    butL.append(but)
    butL[i].grid(row=(8-i)//3,column=(8-i)%3)


win.mainloop()
