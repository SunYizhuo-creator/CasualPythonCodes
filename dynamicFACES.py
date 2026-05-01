from turtle import *
import time

# 定义绘制脸部函数
def draw_face():
    speed(6)
    pensize(4)
    # 画圆脸
    pencolor('orange')
    penup()
    goto(0, -150)
    pendown()
    begin_fill()
    fillcolor('yellow')
    circle(150)
    end_fill()
    hideturtle()
    
# 定义绘制眼睛函数
def draw_eyes():
    pensize(2)
    # 画左眼睛
    pencolor('brown')
    penup()
    goto(60, 45)
    pendown()
    begin_fill()
    circle(25)
    fillcolor('white')
    end_fill()
    pencolor('black')
    begin_fill()
    circle(13)
    fillcolor('black')
    end_fill()
    # 画右眼睛
    pencolor('brown')
    penup()
    goto(-60, 45)
    pendown()
    begin_fill()
    circle(25)
    fillcolor('white')
    end_fill()
    pencolor('black')
    begin_fill()
    circle(13)
    fillcolor('black')
    end_fill()
    hideturtle()
    
# 定义emoji_1函数，绘制微笑表情
def emoji_1():
    draw_face()
    draw_eyes()
    pencolor('brown')
    penup()
    goto(-70,-60)
    pendown()
    right(65)
    pensize(5)
    circle(75,130)
    seth(0)
    hideturtle()
    
# 定义emoji_2函数，绘制难过表情
def emoji_2():
    draw_face()
    draw_eyes()
    pencolor('brown')
    # TODO 抬起画笔
    penup()
    # TODO 将画笔移动到(-70,-80)
    goto(-70,-80)
    # TODO 落下画笔
    pendown()
    # TODO 画笔向右旋转120度
    right(120)
    # TODO 画笔粗细设置为5
    pensize(5)
    # TODO 绘制一个半径为80，圆心角为-120度的圆
    circle(80,-120)
    # TODO 将画笔调至0度
    seth(0)
    # 隐藏画笔
    hideturtle()


i = 1
while i<=2:
    tracer(0)
    emoji_1()
    time.sleep(1)
    update()
    tracer(0)
    emoji_2()
    time.sleep(1)
    update()
    i = i + 1