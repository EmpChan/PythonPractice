"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter.filedialog import *

win = Tk()
win.geometry("400x100")

la = Label(win,text = "선택된 파일 이름")
la.pack()

value = askopenfilename(parent = win,filetypes = (("GIF 파일", "*.gif"),\
                                                  ("모든파일", "*.*")))


la.configure(text = str(value))

win.mainloop()
