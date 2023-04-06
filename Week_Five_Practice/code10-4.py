"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *

win = Tk()

photo = PhotoImage(file = "img1.gif")
la = Label(win,image=photo)

la.pack()


win.mainloop()
