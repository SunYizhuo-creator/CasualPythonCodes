# 导入turtle中的全部函数
from turtle import *
# 使用input()函数引导用户输入表情包语录
# 文案内容为"请输入表情包语录 :"
content = '嘿嘿'
# 定义draw_face()函数绘制脸部
def draw_face():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-120,0)的地方
    goto(-120,0)
    # 落笔
    pendown()
    # 将画笔颜色设置为黑色'black'
    pencolor('black')
    # 将画笔粗细设置为4
    pensize(4)
    # 调整海龟朝向-90度方向
    seth(-90)
    # 开始填充颜色
    begin_fill()
    # 画圆，圆的半径为130，圆心角为360度
    circle(130,360)
    # 填充颜色为'gold'
    fillcolor('gold')
    # 停止填充颜色
    end_fill()
# 定义draw_mouth() 函数绘制嘴巴   
def draw_mouth():
    # 抬起画笔
    penup()
    # 移动到坐标点为(-80,-10)的位置
    goto(-80,-10)
    # 落笔
    pendown()
    # 调整海龟朝向-90度方向
    seth(-90)
    # 绘制一个半径为90，圆心角为180的半圆
    circle(90,180)
# 定义eys_white()函数绘制眼白   
def eyes_white():
    # 使用penup()函数抬起画笔
    penup()
    # 使用forward()函数往前直走60步
    forward(60)
    # 使用seth()函数将角度调整为155度
    seth(155)
    # 使用pendown()函数落笔
    pendown()
    # 使用pensize()函数设置画笔粗细为20
    pensize(20)
    # 使用pencolor()函数设置画笔颜色为'white'
    pencolor('white')
    # 使用circle()函数绘制一个半径为100，圆心角为45的弧形
    circle(100,45)
    # 使用penup()函数抬笔
    penup()
    # 使用seth()函数朝向180度方向
    seth(180)
    # 使用forward()函数向前走40步
    forward(40)
    # 使用seth()函数将角度调整为155度
    seth(155)
    # 使用pendown()函数落笔
    pendown()
    # 使用circle()函数绘制一个半径为100，圆心角为45度的圆弧
    circle(100,45)
    # 使用penup()函数抬笔
    penup()

#  定义一个eyes_black()函数绘制黑眼珠，参数为x
def eyes_black(x):
    # 使用seth()函数将角度设置为0
    seth(0)
    # 使用forward()函数前进x步
    forward(x)
    # 使用pendown()函数落笔
    pendown()
    # 使用pensize()函数设置画笔粗细为15
    pensize(15)
    # 使用pencolor()函数设置画笔颜色为'black'
    pencolor('black')
    # 使用circle()函数绘制一个半径为5，圆心角为360度
    circle(5,360)
    # 使用penup()函数抬笔
    penup()
    # 使用forward()函数前进110步
    forward(110)
    # 使用pendown()函数落笔
    pendown()
    # 使用circle()函数绘制一个半径为5的圆，圆心角为360度
    circle(5,360)
    # 使用hideturtle()函数隐藏画笔
    hideturtle()
    
# 定义一个write_emoji()函数书写文字 
def write_emoji():
    # 使用penup()函数抬起画笔
    penup()
    # 使用fillcolor()函数将填充颜色设置为black
    fillcolor('black')
    # 使用goto()函数移到坐标点为(0,-170)的位置
    goto(0,-170)
    # 使用write()函数设置书写内容
    # 文字内容为love，居中方式为align = "center"，字体类别，大小和粗细为font=('Arial',25,'bold')
    write(content,align = "center",font=('Arial',25,'bold'))     

# 定义一个函数绘制emoji绘制表情，参数x表示移动位置
def emoji(x):
    # 使用draw_face()函数绘制脸部
    draw_face()
    # 使用draw_mouth()函数绘制嘴巴
    draw_mouth()
    # 使用eyes_white()函数绘制白眼珠
    eyes_white()
    # 使用eyes_black(x)函数绘制黑眼珠，参数x表示移动距离
    eyes_black(x)
    # 使用write_emoji()函数书写表情包文字
    write_emoji()
# TODO 导入time函数
import time
# 设置一个计数器，从0开始计数   
n = 0
# 当计数小于10时
while n < 10:
    # 使用tracer()函数，关闭动画
    tracer(0)
    # 绘制表情包1,emoji(6)
    emoji(6)
    # 使用update()函数刷新画面
    update()
    # TODO 使用time.sleep()函数设置停顿时间0.5秒
    time.sleep(0.5)
    # 使用tracer()函数，关闭动画
    tracer(0)
    # 绘制表情包2,emoji(60)
    emoji(60)
    # 使用update()函数刷新画面
    update()
    # TODO 使用time.sleep()函数设置停顿时间0.5秒
    time.sleep(0.5)
    # 计数器加1
    n = n + 1
