""" 070_红色闪烁.py
    我们以前用的是颜色字符串来表示颜色，在 python 海龟画图中我们可以用三个 0~255 的数值来表示一种颜色。
    例：(255, 0, 0) 表示的是红色，(0, 255, 0) 表示的是绿色，(0, 0, 255) 表示的是蓝色。
    用这种方法表示颜色叫 RGB 表示法，在计算机中所有的颜色都是用RGB三种颜色合成的。
    我们把RGB三种颜色都分成256份。让它们的值从 0 到 255，如果R的值为 0 的话，表示红色份量为 0 。
    即没有红色，当红色的份量一直增大到最后为255的时候，就是红色最大的时候。
    绿色和蓝色同理。
    本程序演示的是红色的份量越来越多，小海龟越来越红，它的其它颜色份量都为0。
"""
from turtle import *
bgcolor("black")

red_shiny_turtle = Turtle(visible=True)

red_shiny_turtle.shape("classic")                 # 上节课问题，修改海龟形状，可以是“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”

red_shiny_turtle.getscreen().colormode(255)     # 设定颜色最大值为 255

red_shiny_turtle.fillcolor(255, 0, 0)

while(1):
    pass

red_shiny_turtle.shapesize(5, 5)                # 让海龟变大为原来的 5 倍
red_shiny_turtle.penup()

red_shiny_turtle.goto(-100, 0)
red_shiny_turtle.showturtle()

i = 0

def shine():
    global i                                    # 声明 i 是全局变量，即这里的i是函数外面定义的 i  
    red_shiny_turtle.fillcolor(i, 0, 0)         # 设定龟的填充颜色为 (i, 0, 0)
    i = i + 1
    i = i % 256                                 # 对 255 取余，因为每种颜色份量的最大值只能是 255
    title("当前RGB值：(" + str(i) + ", 0, 0)")
    ontimer(shine, 1)                           # 每 10 毫秒调用一次发光这个函数  

shine()

 






