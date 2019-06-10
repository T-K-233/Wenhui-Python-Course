""" 062_十字架.py
    练习画一个十字架，然后让它旋转。
"""
from turtle import *

print("海龟自带的图形：\n", getshapes())

shape = Turtle()
shape.begin_poly()

for i in range(4):
    shape.fd(100)
    shape.fd(-100)
    shape.right(90)

shape.end_poly()            # 结束记录多边形的顶点。
p = shape.get_poly()        # 得到刚才所画的图形的每个顶点，形成元组，放到变量 p 这里。
register_shape("十字架", p)  # 注册p为正方形的名称，以后就能用它做海龟本身的图形了。
shape.clear()
shape.hideturtle()          # 名字叫"shape"的海龟完成了任务，把它隐藏起来。
del shape                   # 名字叫"shape"的海龟完成了任务，我们不仅仅把它隐藏，而且把它给删除。


cross = Turtle(shape='十字架')
cross.pencolor("blue")
cross.pensize(5)
cross.fillcolor("green")

def rotate_cross():
    cross.right(10)
    ontimer(rotate_cross,10)
rotate_cross()


print("新增十字架后的列表：\n", getshapes())


