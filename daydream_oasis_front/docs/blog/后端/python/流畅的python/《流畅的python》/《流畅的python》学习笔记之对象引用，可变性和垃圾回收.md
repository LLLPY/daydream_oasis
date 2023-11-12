---

next: false

---



<BlogInfo id="777"/>


### **引用式变量**

不知道大家对python中的变量是怎么理解的？
假设有如下代码，怎么理解a和b的关系？


```python
a=1 
b=a
```

![](http://www.lll.plus/media/image/2022/03/24/image-20220324213321-1.png)

没错，正确的理解为第二种，在python中定义一个变量时，并给它"赋值"，其实你并没有真正的把值给它，而是在这个值上贴了一个标签而已，以后看到这个标签就知道是这个值啦！

我们通过id()来验证这一点：

![](https://img-blog.csdnimg.cn/702f5b67fb0641e591db2fc740c098e0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_16,color_FFFFFF,t_70,g_se,x_16)

因此，说python中的变量是 **引用式变量** 再确切不过了！

### **在==和is之间选择**

==运算符比较的是两个对象的值，而is比较对象的标识。下面的这个例子很好的说明了这个问题。

![](https://img-blog.csdnimg.cn/4db9337734ab40fdbb1e316b033fe0f8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_17,color_FFFFFF,t_70,g_se,x_16)

 a和b两个变量分别是两个值相同但地址不同的数组的标签。

值得注意的是，is运算符比==速度快，因为它不能重载，所以python不用寻找并调用特殊方法(魔法方法)，而是直接比较两个整数ID。而a==b是语法糖，等同于a.__eq__(b)。继承自object的__eq__方法比较两个对象的ID，结果与is一样。但是多数内置类型使用更具有意义的方式覆盖了__eq__方法，会考虑对象属性的值。

### **元组的相对不可变性**

你记忆中的元组是不可变类型吗？来看个例子吧！

![](https://img-blog.csdnimg.cn/b21500621d514303bf5649be72a09912.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_19,color_FFFFFF,t_70,g_se,x_16)

 不知道你们的第一想法是不是这样的：咦？不是说元组是不可变类型吗？为什么还能添加新的元素？？？

看到下面的例子也许可以解开你的谜底！

![](https://img-blog.csdnimg.cn/7c9fb5c71f394550a65dc2a472b4157a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_18,color_FFFFFF,t_70,g_se,x_16)

可以看到，在添加元素前后，元组的id是没有发生变化的，也就是说还是同一个元组，并且元组中的最后一个元素（数组）的id也没有发生变化！不知道你们还记不记得：元组属于容器序列，保存的是对象的引用。那么这就说的通了！因为保存的是数组的引用（标签），在素组中添加或者删除元素是没有问题的，而元组中对它的引用是没有改变的。

一句话总结： **元组的值会随着引用的可变对象（比如数组就是可变对象）的变化而变，元组中不可变的是元素的标签（引用）。**


### **浅复制和深复制**  

来看一个例子：

```python
from copy import copy, deepcopy


# 校车乘客在途中上车和下车
class Bus:

    # 初始化
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    # 上车
    def pick(self, name):
        self.passengers.append(name)

    # 下车
    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus = Bus(['Tom', 'Autumn', 'Kim', 'Olivia'])
    bus1 = copy(bus)  # 浅复制得到bus1
    bus2 = deepcopy(bus)  # 深复制得到bus2

    print(id(bus))
    print(id(bus1))
    print(id(bus2))

    bus.pick('Jack')
    print(bus.passengers, id(bus.passengers[0]), id(bus.passengers))
    print(bus1.passengers, id(bus1.passengers[0]), id(bus1.passengers))
    print(bus2.passengers)
```

![](https://img-blog.csdnimg.cn/41cc15bc349548a8965aaae39ce88dfc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

bus是最原始的，bus1通过浅拷贝得到，bus2通过深拷贝得到，在对源bus进行操作时，浅拷贝得到的bus1会受到影响，而深拷贝得到的bus2却不会。

 个人理解：  
        不管是浅复制还是深复制，得到的对象都是新的，但是深复制得到的对象的元素(属性)的值都是新的(另外开辟空间得到的)，而浅复制得到的对象的元素(属性)是对源对象的引用。

### **不要使用可变类型作为参数的默认值**

举一个神奇的栗子看一下！

```python
def _append(a=[]):
    a.append(1)
    return a


if __name__ == '__main__':
    a = _append()  # 如果没有传入参数，则使用默认的值
    print(a)
    a = _append()  # 还是使用的同一个默认参数
    print(a)
```


![](https://img-blog.csdnimg.cn/0539d08512274ffea39e59719f47925c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_13,color_FFFFFF,t_70,g_se,x_16)

不知道结果是不是有点出乎你们的意料？？？为什么不是两个一模一样的数组[1]？通过结果可能就会想到两次方法的调用使用的是同一个数组。没错，就是这样的！首先得知道的一点是：在给函数传参时，传入的是对变量的引用！对于缺省参数也是一样的，上面的这个栗子中，因为没有传入参数，所以使用默认值空列表，而这个默认列表在函数定义时就生成了，也就是说这里是对这个空列表的引用，当第二次调用方法时，因为也没有传入参数，因此还是对这个空列表的引用，所以两次操作的其实是同一个列表，因此得到如上的结果就不意外啦！

个人理解：  
      在未传入参数的情况下，所有的对象会公用默认参数，如果默认参数是可变的，那么后果不堪设想！


### **del和垃圾回收**

del语句删除名称（标签），而不是对象。仅当删除的是最后一个引用时，或无法得到对象时，才会将对象进行垃圾回收。

在Cpython中，垃圾回收使用的主要算法是引用计数。每次给对象添加一个新的标签时，会进行急速加一操作，同理，当进行标签"撕毁"时，就进行减一操作，当一个对象身上没有标签时，计数归零，对象就会被立即销毁。





<ActionBox />
