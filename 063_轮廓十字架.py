""" 063_轮廓十字架.py
    练习画一个带面积的十字架
"""
from turtle import *

print("海龟自带的图形：\n", getshapes())

shape = Turtle()
shape.begin_poly()


for i in range(4):      # 让i依次的值为0，1，2，3，让for语句组重复4次
    shape.fd(10)
    shape.right(90)
    shape.fd(50)
    shape.left(90)
    shape.fd(50)
    shape.right(90)
    shape.fd(10)

shape.end_poly()        # 结束记录多边形的顶点。
