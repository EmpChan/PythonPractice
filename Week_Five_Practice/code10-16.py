"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

def keyevent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키:"+chr(event.keycode))
    
win.bind("<Key>", keyevent)

win.mainloop()
