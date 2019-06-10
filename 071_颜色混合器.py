""" 071_颜色混合器.py

    展示RGB颜色混合。
"""
from turtle import *
r = 0
g = 0
b = 0

bgcolor("black")

red = Turtle(visible=False)
red.getscreen().colormode(255)
red.color('gray100', 'red')      # 分别设定海龟的画笔颜色和填充颜色
red.shapesize(5)                 # 让海龟变大为原来的5倍
red.penup()
red.goto(-100, 0)
red.showturtle()    


green = Turtle(visible=False)
green.getscreen().colormode(255)
green.color('gray100', 'green')
green.shapesize(5)
green.penup()
green.goto(0, 0)
green.showturtle()


blue = Turtle(visible=False)
blue.getscreen().colormode(255)
blue.color('gray100', 'blue')
blue.shapesize(5)
blue.penup()
blue.goto(100, 0)
blue.showturtle()


def red_plus():
    global r, g, b
    r += 5
    r = max(0, min(r, 255))         # 限定r的范围为0到255。
    red.sety(r)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

def red_minus():
    global r, g, b
    r -= 5
    r = max(0, min(r, 255))
    red.sety(r)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

def green_plus():
    global r, g, b
    g += 5
    g = max(0, min(g, 255))
    green.sety(g)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

def green_minus():
    global r, g, b
    g -= 5
    g = max(0, min(g, 255))
    green.sety(g)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")
    
def blue_plus():
    global r, g, b
    b += 5
    b = max(0, min(b, 255))
    blue.sety(b)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

def blue_minus():
    global r, g, b
    b -= 5
    b = max(0, min(b, 255))
    blue.sety(b)
    bgcolor(r, g, b)
    title("当前RGB值：(" + str(r) + ","  + str(g) + "," + str(b) + ")")

screen = red.getscreen()
screen.onkeypress(red_minus, "e")
screen.onkeypress(red_plus, "r")
screen.onkeypress(green_minus, "f")
screen.onkeypress(green_plus, "g")
screen.onkeypress(blue_minus, "v")
screen.onkeypress(blue_plus, "b")


listen()


 






