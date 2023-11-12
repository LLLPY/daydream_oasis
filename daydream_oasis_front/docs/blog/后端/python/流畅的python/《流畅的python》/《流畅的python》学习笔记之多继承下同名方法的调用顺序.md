---

next: false

---



<BlogInfo id="776"/>

###  类名限定法

学习python的小伙伴都知道python是支持多继承的，既然支持多继承就会有一个问题，如果继承的多个父类中含有同名的方法这么办？作为第一门实现多继承的流行语言c++是使用类名限定方法调用来避免这种歧义的。在[《浅谈c++》](http://www.lll.plus/learningPlanet/386#
"《浅谈c++》")一文中有记载：![](https://img-blog.csdnimg.cn/ae1046a93fb24d1f805964cf7debb3e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

那么在Python中也是不是可以采取这种方式呢？来举个栗子看看吧！


```python
# 在多重继承的情况下，如果继承的父类中有同名的方法，在子类中调用时，会根据__mro__中的调用顺序
# 去查找，会调用第一个查找到的方法。

class A:
    def ping(self):
        print(f'A ping', self)


class B(A):
    def pong(self):
        print(f'B pong', self)


class C(A):
    def pong(self):
        print(f'C pong', self)


class D(B, C):  # 继承顺序是B，C，在__mro__的顺序也是B,C，因此当B和C中有同名方法时，优先调用B中的方法

    def pong(self):
        C.pong(self)

if __name__ == '__main__':
    d = D()
    d.pong()
```

![](https://img-blog.csdnimg.cn/c65e14662f7742e58692f79868609e0f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

可以看到，在B类和C类中，都有自己定义的pong()方法，但是在子类D中，直接使用C.pong(self)刻意调用了C类中定义的pong方法，并且正确显示了！
**所以可以使用类名限定的方法解决多继承方法名冲突的问题！**

### mro(method resolution order)指定方法调用顺序

大多数情况下，使用类名限定的方法会限制很多！比如在简化代码时，发现某一个类其实是多余的，但是在其子类中使用了类名调用了该类的某一个方法，如果想要删除这个类，就必须去动其子类，因此在大部分情况下，还是会使用super()方法动态的调用父类中的方法，而在多继承同名的方法中，具体调用哪一个类中的方法就得看__mro__属性了！
再来看一个栗子吧！


```python
class A:
    def ping(self):
        print(f'A ping', self)

class B(A):
    def pong(self):
        print(f'B pong', self)

class C(A):
    def pong(self):
        print(f'C pong', self)

class D(B, C):  # 继承顺序是B，C，在__mro__的顺序也是B,C，因此当B和C中有同名方法时，优先调用B中的方法

    def pong(self):
        super().pong()

if __name__ == '__main__':
    d = D()
    d.pong()
    print(D.__mro__)
```


还是相同的栗子，注意查看类D中继承类B和类C的书写顺序！

![](http://www.lll.plus/media/image/2022/04/07/image-20220407183553-1.png)

可以看到mro中指定类的调用顺序和书写的继承顺序是一致的！如果类B写在类C的前面，那么优先调用类B中的方法；同理如果类C写在类B的前面，优先调用类C中的方法。当然，前提是自己的类中没有定义该方法！

### 子类化内置类型中的一个天坑！

有些时候我们可能会感觉一些内置类型和我们的需求还有一定的距离，于是就会在原有的基础上进行封装，来看看下面这个栗子：


```python
# 内置类型dict的__init__和__update__方法会忽略我们覆盖的__setitem__方法

'''

直接子类化内置类型（如dict，list和str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法。

'''

# 继承自内置类型dict
class DoppelDict(dict):

    # 覆盖父类的__setitem__方法
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

    # 在__getitem__找不到键的情况下会调用__missing__方法，如果该方法存在的话
    def __missing__(self, key):
        self[key] = 0
        return 0


if __name__ == '__main__':
    dd = DoppelDict(one=1)  # __init__方法没有调用我们重定义的__getitem__方法
    print(dd)
    dd['two'] = 2  # 调用了我们覆盖的__setitem__
    print(dd)

    dd.update(three=3)  # update没有调用我们的覆盖的__setitem__
    print(dd)

```

![](https://img-blog.csdnimg.cn/f824c19211bb406a90e6352daf917e4d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 在这个栗子中，我们的目的可能是在给字典添加一个新的值的时候都对其值进行乘2操作，但是实际情况确实，在实例化和update时都未使用我们覆写的方法！

那么为什么会这样呢？原因在于 **内置类型的方法通常会忽略用户覆盖的方法** 。

那这样是不是违背了mro的调用顺序？

从显示结果来看，确实违背了调用顺序！但是这么明显的结果，难道设计者没有想到这一点吗？答案是肯定的！
**但根本的原因还是在于考虑到python的性能！内置的dict，list和str类型都是python的底层基础，因此速度必须快！与这些内置类型有关的任何性能问题几乎都会对其他所有代码产生大影响！**
于是，Cpython走了一个捷径，故意让内置类型的方法行为不当，即不调用被子类覆盖的方法。

因此，任何事情都不能绝对的，看似完美的mro方法解决了多继承下同名方法的调用问题，但是如果python底层的类型也走这个套路的话，会给其带来性能上的问题，比较两者，择其优者而从之！


### 但是，上帝在给你关上一扇门的同时，会给你打开另一扇窗的！

在collections库中，也同样封装了类似于dict，list和str的类型：UserDict，UserList和UserString,虽然它们的速度没有内置类型的快，但是它们是不会出现上面的问题的，扩展性开始比较强的！如果你的看到这里了，快去试试这些类型吧！






<ActionBox />
