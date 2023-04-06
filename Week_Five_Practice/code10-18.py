"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    win.quit()
    win.destroy()

mainMenu = Menu(win)
win.config(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = filemenu)
filemenu.add_command(label = "열기", command = func_open)
filemenu.add_separator()
filemenu.add_command(label = "종료", command = func_exit)

win.mainloop()
