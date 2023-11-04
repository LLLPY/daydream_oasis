
<BlogInfo id="773" title="《流畅的python》学习笔记之偏心的python！" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="70" category="《流畅的python》" tag_list="['']" create_time="2022.04.02 12:27:49.239660" update_time="2022.07.11 10:42:08" />



### **一些 "蹊跷"的对象**

不知道大家有没有想过为什么有的对象可以使用for循环进行迭代，可以使用in判断它是否包含某个元素，可是使用索引进行取值.....

没错，答案就是这些对象实现了支持这些操作的特殊方法！

比如，实现了__iter__方法，就可以对该对象进行迭代操作。


```python
class MyList:

    def __init__(self, *args, **kwargs):
        self.li = list(args)


if __name__ == '__main__':
    my_list = MyList(1, 2, 3, 4)
    for i in my_list:
        print(i)
```


![](../media/image/2022/04/02/image-20220402122735-1.png)

实现__iter__方法后


```python
class MyList:

    def __init__(self, *args, **kwargs):
        self.li = list(args)

    def __iter__(self):
        return iter(self.li)  #将li转换成一个迭代器并返回


if __name__ == '__main__':
    my_list = MyList(1, 2, 3, 4)
    for i in my_list:
        print(i)
```


![](https://img-blog.csdnimg.cn/548906d4b301410897fc29a0099dd6f1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

其他功能的对应实现方法 可以迭代，比如使用for | __iter__()  
---|---  
可以使用in | __contains__()  
可以通过索引取值 | __getitem__()  
  
### **但是，python对序列有偏心！**

为什么这么说呢？来看一个栗子吧！


```python

# 举个栗子
class Dog:

    def __getitem__(self, item):
        return [f'dog{i}' for i in range(0, 5)][item]


if __name__ == '__main__':

    # 实例化一个对象
    dog = Dog()

    # 迭代
    for i in dog:
        print(i)

    # in方法
    print('dog3在dog里面：', 'dog3' in dog, 'dog10在dog里面：', 'dog10' in dog)

    # 索引取值
    print(dog[0])
```


![](https://img-blog.csdnimg.cn/21840415e6b443ee8309df0ff8638e62.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 所以为什么说python喜欢序列？现在应该知道了吧！  
**原因很简单，在一个对象中，就算没有实现__contains__和__iter__方法，只要实现  
了__getitem__方法，就可以正常使用in,就可以正常迭代对象！这不是纯纯的偏心吗？！**  


可能看到这里的小伙伴有点迷茫，产生这样的迷惑：这个栗子和序列有什么关系？

因为在python中，我们说一个对象是序列，往往不是因为它就是序列，而是因为它的行为像序列。而在一个对象中，如果实现了__getitem__方法，它就可以通过索引取值，而这种行为是序列的行为，所以上述的Dog（可能这个名字取得不太好，和队列一点关系都没有仿佛），我们也可以说它是一个序列！

