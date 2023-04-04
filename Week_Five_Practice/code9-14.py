# -*- coding: utf-8 -*-
"""
이름 : 황재찬
학번 : 2020039040
"""

import My as my
import turtle as t

swidth,sheight = 300,300
tx,ty,tangle,tsize = [0]*4

t.title('거북이 글자쓰기(모듈버전)')
t.shape('turtle')
t.setup(width = swidth+50,height = sheight +50)
t.screensize(swidth,sheight)
t.penup()
t.speed(0)

inStr = my.getString()

for ch in inStr:
    tx,ty,tangle,tsize = my.getXYAS(swidth, sheight)
    
    t.goto(tx,ty)
    t.left(tangle)
    
    t.pencolor(my.getRGB())
    t.write(ch,font=('맑은고딕',tsize,'bold'))

t.done()
