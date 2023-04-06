"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *

win = Tk()

la_1 = Label(win,text = "COOKBOOK~~Python을")
la_2 = Label(win, text = "열심히",\
             font = ("궁서체",30), fg = "blue")
la_3 = Label(win, text = "공부중입니다.", \
             bg = "magenta",width = 20,height = 5,\
             anchor = SE)

la_1.pack()
la_2.pack()
la_3.pack()

win.mainloop()
