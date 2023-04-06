"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

def click(event):
    txt=''
    if event.num == 1:
        txt = "mouse left button ("
    elif event.num == 3:
        txt = "mouse right button ("
    txt += str(event.y) +',' + str(event.x) + ") clicked"
    la.configure(text = txt)
la = Label(win,text = "이곳이 바뀜")
win.bind("<Button>", click)
la.pack(expand=1,anchor = CENTER)
win.mainloop()
