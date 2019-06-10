"""059_动态背景配音_春晓.py
要求掌握数组、函数迭代和异步音频播放概念
"""
from winsound import PlaySound, SND_ASYNC
from turtle import *
from time import sleep

music_file = "assets/春晓.wav"

# 定义一个数组，里面包含了四个背景图片的文件名
background_images = ["assets/下雨001.png", "assets/下雨002.png", "assets/下雨003.png", "assets/下雨004.png"]

index = 0

t = Turtle()
t.hideturtle()
t_screen = t.getscreen()                # 得到海龟 t 所在的画图屏幕, get 是得到的意思，screen 是屏幕的意思。
t_screen.setup(700, 500)                # 设定屏幕分辨率为 700 像素 x 500 像素


def change_background_animation():      # 定义一个更换背景的函数
    global index
    t_screen.bgpic(background_images[index])            # 更换海龟 t 的屏幕的背景图像
    index = index + 1
    index = index % 4                                   # 使 index 永远不大于 4
    
    # 在 .ontimer 方法中执行自己，相当于死循环，一直隔 100 毫秒执行下去
    t_screen.ontimer(change_background_animation, 100)


change_background_animation()

PlaySound(music_file, SND_ASYNC)        # 异步播放音效，注意 SND_ASYNC 这个旗帜的用法

t.penup()
t.goto(-100, 100)
t.pencolor("white")
t.write("春晓", font=("", 24, "bold"))
t.sety(t.ycor() - 50)
sleep(1)
t.write("---------孟浩然", font=("", 14, "bold"))
t.sety(t.ycor() - 50)
sleep(1)
t.write("春眠不觉晓", font=("", 24, "bold"))
t.sety(t.ycor() - 50)
sleep(1)
t.write("处处闻啼鸟", font=("", 24, "bold"))
t.sety(t.ycor() - 50)
sleep(1)
t.write("夜来风雨声", font=("", 24, "bold"))
t.sety(t.ycor() - 50)
sleep(1)
t.write("花落知多少", font=("", 24, "bold"))


    
