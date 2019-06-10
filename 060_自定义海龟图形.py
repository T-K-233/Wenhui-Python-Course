""" 060_自定义海龟图形.py
    python 的海龟画图能加载外部的图片做为海龟本身的图形，也能自己画一个图做为海龟对象的形状。
    海龟的图形存放在一个列表里，我们能用 getshapes() 命令查看这个列表里有些什么图形。
    本节课让海龟首先画一个正方形，然后把这个正方形做为海龟本身的图形。
"""
from turtle import *

print("海龟自带的图形：\n", getshapes())

shape = Turtle()        # 新建 "shape" 海龟，它的使命就是画一个正方形，然后被注册到海龟的图形列表。
shape.begin_poly()      # 开始记录多边形的顶点，当前的海龟位置是第一个顶点，做为图形旋转中心。
shape.begin_fill()      # 开始填充图形，不填充也是可以的。

for i in range(4):      # 让 i 依次的值为 0, 1, 2, 3，让 for 语句组重复 4 次
    shape.forward(100)
    shape.right(90)

shape.end_fill()        # 结束填充 
shape.end_poly()        # 结束记录多边形的顶点。
p = shape.get_poly()    # 得到刚才所画的图形的每个顶点，形成元组，放到变量 p 这里。


print("p:", p)
print()
print("p 是一个元组，它记录了多边形的每个顶点的坐标值。")
register_shape("正方形", p)    # 注册"正方形"为 p 形状的名称，以后就能用它做海龟本身的图形了。


shape.clear()
shape.hideturtle()      # 名字叫'形状'的海龟完成了任务，把它隐藏起来。
del shape               # 名字叫'形状'的海龟完成了任务，我们不仅仅把它隐藏，而且把它给删除。


# 下面是建立一个叫正方形1的海龟对象，让它的形状为刚才定义的正方形。
square = Turtle(shape="正方形")
square.pencolor("cyan")
square.fillcolor("green")

def rotate_square():
    square.right(10)
    ontimer(rotate_square, 10)
    
rotate_square()


# 问题：
# 既然 p 是一个元组，里面存储的是每个坐标点，那么我们能不能自己直接定义一个有各个顶点的元组呢？
# 所以，我们不必要新建所谓的‘形状’海龟了
# 我们直接定义一个元组即可，下面是一个例子
# 这里定义一个元组也叫 p ,它的第一个项目是(0, 0)，第二个项目是(0, 100)
# 当用 register_shape 注册时它的第一个项目就是旋转中心。

p = ((0, 0), (0, 100))
addshape("线段", p)           # 也可以用 addshape("线段", p)
print("\n所有的形状为：", getshapes())

line = Turtle(shape="线段")
line.pensize(5)
line.pencolor("red") 
line.penup()
line.goto(0, 200)

def rotate_line():
    line.right(10)
    ontimer(rotate_line, 10)

rotate_line()









