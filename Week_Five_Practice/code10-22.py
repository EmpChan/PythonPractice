"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter.filedialog import *

def func_open():
    filename = askopenfilename(parent = win,filetypes = (("GIF 파일", "*.gif"),\
                                                  ("모든파일", "*.*")))
    photo = PhotoImage(file = filename)
    pl.configure(image = photo)
    pl.image = photo

def func_exit():
    win.quit()
    win.destroy()

win = Tk()
win.geometry("400x400")
win.title("유우머코드")

photo = PhotoImage()
pl = Label(win,image=photo)
pl.pack(expand =1,anchor = CENTER)

mainMenu = Menu(win)
win.config(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = filemenu)
filemenu.add_command(label = "열기", command = func_open)
filemenu.add_separator()
filemenu.add_command(label = "종료", command = func_exit)

win.mainloop()
