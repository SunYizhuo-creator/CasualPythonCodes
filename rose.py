from turtle import *

# 设置初始位置
penup()
left(90)
forward(130)
pendown()
right(90)

# 绘制花蕊
fillcolor("red")
begin_fill()
circle(10,180)
circle(25,110)
left(50)
circle(60,45)
circle(20,170)
right(24)
forward(30)
left(10)
circle(30,110)
forward(20)
left(40)
circle(90,70)
circle(30,150)
right(30)
forward(15)
circle(80,90)
left(15)
forward(45)
right(165)
forward(20)
left(155)
circle(150,80)
left(50)
circle(150,90)
end_fill()

# 绘制第一片花瓣
left(150)
circle(-90,70)
left(20)
circle(75,105)
seth(60)
circle(80,98)
circle(-90,40)

# 绘制第二片花瓣
# TODO 向左旋转180度
left(180)
# TODO 绘制半径为90，圆心角为40度的圆
circle(90,40)
# TODO 绘制半径为-80，圆心角为98度的圆
circle(-80,98)
seth(-83)

# 绘制第一片叶子
forward(30)
left(90)
forward(25)
left(45)
fillcolor("green")
begin_fill()
circle(-80,90)
right(90)
circle(-80,90)
end_fill()
right(135)
forward(30)
left(180)
forward(55)
left(90)
forward(30)

# 绘制第二片叶子
right(90)
right(45)
fillcolor("green")
begin_fill()
# TODO 绘制半径为80，圆心角为90度的圆
circle(80,90)
# TODO 向左旋转90度
left(90)
# TODO 绘制半径为80，圆心角为90度的圆
circle(80,90)
end_fill()
left(135)
# TODO 画笔前进30
forward(30)
# TODO 向左旋转180度
left(180)
# TODO 画笔前进30
forward(30)
# TODO 向右旋转90度
right(90)
# TODO 绘制半径为130，圆心角为60度的圆
circle(130,60)