"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

mainMenu = Menu(win)
win.config(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = filemenu)
filemenu.add_command(label = "열기")
filemenu.add_separator()
filemenu.add_command(label = "종료")

win.mainloop()
