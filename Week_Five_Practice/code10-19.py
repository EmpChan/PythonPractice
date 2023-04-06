"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter.simpledialog import *

win = Tk()
win.geometry("400x100")

la = Label(win,text = "입력된 값")
la.pack()

value = askinteger("확대배수","주사위 숫자를 입력하세요."\
                    , minvalue= 1, maxvalue = 6)

la.configure(text = str(value))

win.mainloop()
