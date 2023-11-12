---

next: false

---



<BlogInfo id="698"/>

## turtle—见证小海龟的浪漫之画

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719090628717.jpg)

最近一直在学习人工智能相关的内容,每天都是枯燥,抽象的概念,数学公式,算法等等,一想到今天又要学习那些东东,我不禁地哽咽了一下,然后脑子里不停地蹦出各种奇怪的想法:‘啊!救救孩子吧!孩子脑容量不够了!’,‘我的大脑会不会因此窒息啊!!’,‘能别让再看到这些东东吗?’,‘再这样学下去我会不会疯掉呀??’  
有没有和我相同境遇的人儿~  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719091954593.gif)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719091954593.gif)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719091954593.gif)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719091954593.gif)  
于是就打算给自己的大脑放个假,学点不伤脑子的东西!(ps:大脑:算你还有点人性!)  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719092449567.gif)  
所以今天的内容特别简单,我找了一个我之前没有学习的库—turtle,这个库是python的版本更新到3.8之后才出来的,也算是一个Python的基础库吧我感觉,非常简单,我是3.6开始学的Python,所以之前没有学习,首先,简单介绍一下这个库:  
[海龟绘图很适合用来引导孩子学习编程。 最初来自于 Wally Feurzeig, Seymour Papert 和 Cynthia Solomon 于1967 年所创造的 Logo 编程语言。通过组合使用此类命令，可以轻松地绘制出精美的形状和图案。turtle 模块是基于 Python 标准发行版 2.5 以来的同名模块重新编写并进行了功能扩展。  新模块尽量保持了原模块的特点，并且(几乎)100%与其兼容。这就意味着初学编程者能够以交互方式使用模块的所有命令、类和方法——运行 IDLE 时注意加 -n参数。turtle 模块提供面向对象和面向过程两种形式的海龟绘图基本组件。由于它使用 tkinter 实现基本图形界面，因此需要安装了 Tk 支持的 Python版本。](https://docs.python.org/zh-cn/3/library/turtle.html)

简单来说,海龟绘图最初是一门logo编程语言,非常适合引导儿童学习编程,通过简单的命令就可以画出精美的图案.  
看到没, **非常适合儿童编程!!!**  
所以今天,也让我们来体验体验一下当小孩的快乐哈哈哈哈~  
简单介绍一下在turtle中的一些基本操作:  

```python
Turtle 方法  
海龟动作  
移动和绘制  
forward() | fd() 前进  
backward() | bk() | back() 后退  
right() | rt() 右转  
left() | lt() 左转  
goto() | setpos() | setposition() 前往/定位  
setx() 设置x坐标  
sety() 设置y坐标  
setheading() | seth() 设置朝向  
home() 返回原点  
circle() 画圆  
dot() 画点  
stamp() 印章  
clearstamp() 清除印章  
clearstamps() 清除多个印章  
undo() 撤消  
speed() 速度  
获取海龟的状态  
position() | pos() 位置  
towards() 目标方向  
xcor() x坐标  
ycor() y坐标  
heading() 朝向  
distance() 距离  
设置与度量单位  
degrees() 角度  
radians() 弧度  
画笔控制  
绘图状态  
pendown() | pd() | down() 画笔落下  
penup() | pu() | up() 画笔抬起  
pensize() | width() 画笔粗细  
pen() 画笔  
isdown() 画笔是否落下  
颜色控制  
color() 颜色  
pencolor() 画笔颜色  
fillcolor() 填充颜色  
填充  
filling() 是否填充  
begin_fill() 开始填充  
end_fill() 结束填充  
更多绘图控制  
reset() 重置  
clear() 清空  
write() 书写  
海龟状态  
可见性  
showturtle() | st() 显示海龟  
hideturtle() | ht() 隐藏海龟  
isvisible() 是否可见  
外观  
shape() 形状  
resizemode() 大小调整模式  
shapesize() | turtlesize() 形状大小  
shearfactor() 剪切因子  
settiltangle() 设置倾角  
tiltangle() 倾角  
tilt() 倾斜  
shapetransform() 变形  
get_shapepoly() 获取形状多边形  
```

当然方法不止这些,看起来非常多,但是其实很多功能都是重复的,比如后退的方法它就有三个:backward() | bk() | back()
,这三个方法只是名字不同而已,实现的功能完全一样,所以这样看来其实也没有多少内容(要不然我也不可能几个小时就看完了它的文档)  
经常在网上看到一箭穿心的的那个图片,比如下面这个:  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719094406265.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
于是我就突发奇想,要不来一个"一箭双雕"吧,正所谓好事成双对,doublekill听起来不是更悦耳一些吗?  
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021071909490284.png)  
所以"一箭双雕"如下;  
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210719095025152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heF9MTEw=,size_16,color_FFFFFF,t_70)  
爱心中的名字可以自己进行修改,源码如下:
```python
from turtle import *

shape('turtle')
# 爱心
def heart(pos, pencolor, fillcolor, text=None):
    speed(6)
    hideturtle()
    up()
    width(3)
    setpos(pos[0], pos[1])
    setheading(0)
    down()
    showturtle()
    color(pencolor, fillcolor)
    left(45)
    begin_fill()
    fd(140)
    for i in range(200):
        left(1)
        forward(1)
    right(135)
    for i in range(200):
        left(1)
        forward(1)
    fd(140)
    end_fill()
    up()
    sety(120 + pos[1])
    down()
    hideturtle()
    color('black', fillcolor)
    write(text, move=False, align='right', font=('黑体', 20, 'normal'))
    showturtle()

# 弓箭
def arrow(pos, pencolor, fillcolor):  # 位置 笔的颜色 填充色 角度
    up()
    width(3)
    setpos(pos[0], pos[1])
    setheading(0)
    color(pencolor, fillcolor)

    down()
    width(10)
    left(30)

    fd(40)
    up()
    fd(290)
    down()
    fd(50)
    begin_fill()
    left(90)
    fd(20)
    right(120)
    fd(40)
    right(120)
    fd(40)
    right(120)
    fd(20)
    end_fill()


def draw(name1='罗密欧',name2='朱丽叶'):
    x = 100
    y = -50
    heart((-200 + x, 0 + y), 'blue', 'blue', name1)
    heart((-80 + x, 20 + y), 'pink', 'pink', name2)
    arrow((-300 + x, 50 + y), '#c2272d', '#c2272d')
    hideturtle()
    done()

if __name__ == '__main__':
    name1=textinput('提示','请输入第一个人的名字:')
    name2=textinput('提示','请输入第二个人的名字:')
    draw(name1,name2)
```
因为源码相对比较简单,就不一一解释了,自己亲自动手试试吧,让绘画大师小海龟为某某和某某留下这甜蜜的一刻吧~

    





<ActionBox />
