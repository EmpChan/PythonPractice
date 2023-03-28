"""
이름 : 황재찬
학번 : 2020039040
"""

import turtle
import random

myt,tx,ty,tcolor,tsize,tshape = [None]*6
shapelist = []
playerturtles = []
swidth,sheight = 500,500

if __name__ == "__main__" :
   turtle.title("거북 리스트 활용")
   turtle.setup(width =swidth+50, height = sheight + 50)
   turtle.screensize(swidth,sheight)
   shapelist = turtle.getshapes()
   for i in range(0,100):
       random.shuffle(shapelist)
       myt = turtle.Turtle(shapelist[0])
       tx = random.randrange(-swidth/2,swidth/2)
       ty = random.randrange(-sheight/2,sheight/2)
       r = random.random()
       g = random.random()
       b = random.random()
       tsize = random.randrange(1,3)
       playerturtles.append([myt,tx,ty,tsize,r,g,b])
   
   for i in playerturtles:
       myt = i[0]
       myt.color((i[4],i[5],i[6]))
       myt.pencolor((i[4],i[5],i[6]))
       myt.turtlesize(i[3])
       myt.goto(i[1],i[2])
   turtle.done()
      
