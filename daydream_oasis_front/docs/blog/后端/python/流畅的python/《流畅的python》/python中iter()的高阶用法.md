---

next: false

---



<BlogInfo id="765"/>

#  前言

众所周知，在python中，iter()函数的功能是：接受一个可迭代对象，将其转换成一个迭代器。

举个栗子：


```python
a=[1,2,3]
a_iter=iter(a)
print(a_iter)
print(next(a_iter))
print(next(a_iter))
```

![](http://www.lll.plus/media/image/2022/04/18/image-20220418103318-1.png)

上面就是iter()的一般用法。

# iter()的高阶用法

但是，iter()还有一个更好玩的用法！

简单做一下描述：传入两个参数：使用常规的函数或者任何可调用的对象创建迭代器。这样使用时， **第一个参数必须是可调用的对象（无参数调用）**
，用于不断调用产出值， **第二个是哨符，这个是标记值** ，当可调用的对象返回这个值时，触发迭代器抛出StopIteration异常，程序结束！
一句话概括一下： **第一个参数中的对象不断产出值，如果产出的值和第二个参数是一样的，就停止产出！**

举个栗子：

随机产生1到10的数字，如果产出数字是5就停止。


```python
from random import randint

def d10():
    return randint(1, 10)


# 随机产生1~10之间的数，遇到5就停止
for i in iter(d10, 5):
    print(i)
```


![](https://img-blog.csdnimg.cn/acc578d29a674c2f9a419d1a69905425.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_16,color_FFFFFF,t_70,g_se,x_16)

 是不是感jio很新鲜，快去亲手试一试吧！






<ActionBox />
