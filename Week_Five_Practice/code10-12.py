"""
이름 : 황재찬
학번 : 2020039040
"""
from tkinter import *
from tkinter import messagebox

win = Tk()

n = 0

def gonext():
    global n
    n +=1
    n %=9
    photo = PhotoImage(file = "img"+str(n+1)+".gif")
    la.configure(image = photo)
    la.image = photo

def goprev():
    global n
    n +=8
    n %=9
    photo = PhotoImage(file = "img"+str(n+1)+".gif")
    la.configure(image = photo)
    la.image = photo
    
photo = PhotoImage(file = "img1.gif")
la = Label(win, image = photo)
but_next = Button(win,text = "다음", command = gonext)
but_prev = Button(win,text = "이전", command = goprev)

but_prev.place(x = 250, y = 10)
but_next.place(x = 400, y = 10)
la.place(x = 15, y= 50)

win.mainloop()
