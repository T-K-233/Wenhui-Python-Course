""" 072_颜色混合器.py

     本程序也能做为RGB颜色展示用途。  
"""
from turtle import *
r = 0
g = 0
b = 0

bgcolor("black")

红龟 = Turtle(visible=False)
红龟.getscreen().colormode(255)
红龟.color('gray100', 'red')      # 分别设定海龟的画笔颜色和填充颜色
红龟.shapesize(5)                 # 让海龟变大为原来的5倍
红龟.penup()
红龟.goto(-100, 0)
红龟.showturtle()

def 红色变换(x, y):       #作为ondrag的事件处理函数，它一定要有x和y参数，接收鼠标的x,y坐标。   
    global r, g, b
    r = max(0, min(y, 255))           #限定r的范围为0到255。
    红龟.sety(r)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")
    


绿龟=Turtle(visible=False)
绿龟.color('gray100',(0,255,0))      #分别设定海龟的画笔颜色和填充颜色
绿龟.shapesize(5)                #让海龟变大为原来的5倍
绿龟.penup()
绿龟.goto(0,0)
绿龟.showturtle()

def 绿色变换(x,y):       #作为ondrag的事件处理函数，它一定要有x和y参数，接收鼠标的x,y坐标。   
    global r,g,b
    g=max(0,min(y,255))           #限定r的范围为0到255。
    绿龟.sety(g)
    bgcolor(r,g,b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

蓝龟 = Turtle(visible=False)
蓝龟.color('gray100','blue')      #分别设定海龟的画笔颜色和填充颜色
蓝龟.shapesize(5)                #让海龟变大为原来的5倍
蓝龟.penup()
蓝龟.goto(100, 0)
蓝龟.showturtle()

def 蓝色变换(x, y):       #作为ondrag的事件处理函数，它一定要有x和y参数，接收鼠标的x,y坐标。   
    global r, g, b
    b = max(0, min(y, 255))           #限定r的范围为0到255。
    蓝龟.sety(b)   
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) +  ","  + str(g) + "," + str(b) + ")")
    
    


红龟.ondrag(红色变换)   #拖动事件发生时，调用红色变换函数，这个函数会接受鼠标的坐标。
绿龟.ondrag(绿色变换)   #拖动事件发生时，调用红色变换函数，这个函数会接受鼠标的坐标。
蓝龟.ondrag(蓝色变换)   #拖动事件发生时，调用红色变换函数，这个函数会接受鼠标的坐标。
listen()


 






