
<BlogInfo id="1301" title="《流畅的python》学习笔记之函数装饰器和闭包" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=214 category="《流畅的python》" tag_list="['基础', '闭包', '装饰器']" create_time="2022.03.22 18:56:39.238598" update_time="2022.07.11 10:42:46" />

###  定义

首先来看一下它们各自的定义

**闭包** ： 闭包
指延伸了作用域的函数，其中包含函数定义体中引用，不在定义体中定义的非全局变量。函数是不是匿名的没有关系，关键是它能访问定义体以外的非全局变量。

例：利用闭包实现一个动态求平均值的功能

```python
# 闭包指延伸了作用域的函数，其中包含函数定义体中引用，同时包含不在定义体中定义的非全局变量。
# 关键是它能访问定义体之外定义的非全局变量！！！
# 利用闭包实现avg(num)：计算不断增加系列值的均值
def make_avager():
    history = []
    def avg(num):
        history.append(num)
        return sum(history) / len(history)

    return avg

if __name__ == '__main__':
    avg = make_avager()
    print(avg(1))
    print(avg(2))
    print(avg(3))
    print(avg(4))
    print(avg(5))

    #avg.__closure__中的各个元素对应于avg.__code__.co_freevars中的一个名称
    print(avg.__code__.co_freevars)
    print(avg.__closure__) #对应于history
    print(avg.__closure__[0].cell_contents) #history的值
```


![](../media/image/2022/03/22/image-20220322185624-1.png)

hsitory的绑定在返回的avg函数的__closure__属性中。avg.__closure__中的各个元素对应于avg.__code__.co_freevars中的一个名称。这些元素是cell对象，有个cell_contents属性，保存着真正的值。

有没有小伙伴很好奇，在创建avg后，第一次调用avg(1)可以求得平均值为1.0，但是第二次在调用avg(2)的时候，按照正常的来应该会报错呀，因为在一个函数执行完成之后，函数里面的变量会自动被回收，为什么第二次执行avg(2)的时候还能找到history的值？？没错，这也是闭包的特性所在！正常函数执行完毕后,里面声明的变量被垃圾回收处理掉,但是闭包可以让作用域里的变量,在函数执行完之后依旧保持在没有被垃圾回收处理掉的状态。

**装饰器** ：装饰器是可调用对象，起参数是另一个函数，装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

个人理解：就是在不改变函数的源码的基础上为其添加额外的功能。



例：实现一个计算函数运行时间的装饰器


```python
import time
from functools import wraps

# 一个简单的装饰器，输出函数的运行时间
def clock(func):
    @wraps(func)  # wraps装饰器会把__name__,__doc__等属性，从func(被装饰的函数)复制给clocked(实际运行的函数)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)  # 通过*args获取func的参数
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(str(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def factorial(n=1):
    #利用递归实现计算前n项和
    return 1 if n < 2 else n + factorial(n - 1)


if __name__ == '__main__':
    print(factorial(100))
    print(factorial.__name__)
```

![](https://img-blog.csdnimg.cn/33d91713bd8d4f6f9f327e2a22f271bd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 上面的
@clock
def factorial(n=1):
        pass
其实就等价于clock(factorial)，真正执行的是clock中的clocked函数。

**wraps装饰器**

细心地小伙伴可能已经看到了在clocked函数定义的上方使用了wraps装饰器，原因是什么呢？原因在于被修饰的函数的__name__，__doc__等属性都会被clocked函数（真正执行的函数）覆盖掉了，如果想要知道被修饰器的函数这些属性就必须通过这个装饰器将被修饰的函数的这些属性复制给clocked函数（真正执行的函数）。

**参数化的装饰器**

解析源码中的装饰器时，Python把被装饰的函数作为第一个参数传给装饰器函数。那怎么让装饰器接受其他参数呢？答案是：创建一个装饰器工厂函数，把参数传给他，返回一个装饰器，然后把它应用到要装饰的函数上。（个人理解：就是在装饰器函数外面再套一层函数，这个函数可以进行传参，但是它的返回值一定要是装饰器函数）。

一个简单的例子

```python
# 根据flag来决定是否打印函数名
def print_func_name(flag=False):  # 装饰器加工厂

    def decorate(func):  # 真正的装饰器
        if flag:
            print(f'因为flag=True，所以打印了{func.__name__}')
        return func
    return decorate


@print_func_name(flag=True)
def hello(word):
    print(f'hello {word}')


@print_func_name()
def say(word):
    print(f'say {word}')


if __name__ == '__main__':
    hello('python')
    say('hello')
```

![](https://img-blog.csdnimg.cn/e7991356166541c2b269873ce1fc8536.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_17,color_FFFFFF,t_70,g_se,x_16)

#### 两个重要的装饰器！

##### 1.使用functools.lru_cache做备忘

functools.lru_cache是非常实用的装饰器，它实现了备忘功能，会自动把耗时的函数结果保存起来，避免传入相同的参数时进行重复的计算！对于递归来说简直就是锦上添花！！！

例：利用递归求斐波那契数列的第n个值

```python
from functools import lru_cache

from lll05_实现一个简单的装饰器 import clock

aa = 1e9 + 7

'''
lru_cache会把耗时的函数结果存储起来，避免传入相同的参数时重复计算，它
有一个参数maxsize=128(为了得到最佳性能，maxsize应该设为2的幂),指明
了存储的最多结果；缓存满了之后，旧的结果会被扔掉。另一个参数typed=False,
如果设为了Ture，会把不同参数类型的结果分开保存(例如1和1.0)

lru的全称时Least Recently Used，缓存不会无限制增加，一段时间不用的缓存条目会被自动删除

'''


# 斐波那契数列
@lru_cache(300)
@clock
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return int((fibonacci(n - 1) + fibonacci(n - 2)) % aa)


if __name__ == '__main__':
    print(fibonacci(10))
```

![](https://img-blog.csdnimg.cn/40c61bf6fe4c42529dab2de9f7dc389a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_15,color_FFFFFF,t_70,g_se,x_16)
![](https://img-blog.csdnimg.cn/206a9e61cc104113ad349bafecbfc83d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_13,color_FFFFFF,t_70,g_se,x_16)

可以很明显的看到在未使用lru_cache装饰器的情况下进行了非常多的重复计算，因此效率非常的低！

#####  2.单分派泛函数装饰器

假如有这么一个要求，写一个函数，对于传入的不同参数类型做不同的操作。

第一想法你可能会想到使用if，else判断参数的类型，多写几个分支来完成。这样做也不是不行，但是那你是不是得把参数所有的类型先穷举出来？因为如果哪天遇到了一个新参数类型单数没有写入if条件中，那岂不是一个bug。所以这样看来，这样实现的函数扩展性和可维护性都很低，并且写出来的代码可能会显得非常的臃肿！singledispatch装饰器就是用来帮助解决这个问题的！

看个例子吧！


```python
from functools import singledispatch

# 个人感觉：该功能类似于c++中的函数重载，根据不同的函数签名调用不同的函数
'''
根据参数的类型调用(分派)对应的功能函数
'''

@singledispatch
def print_obj(obj):
    print(f'这是一个{type(obj)}对象')

@print_obj.register(int)
def _(obj):
    print(f'这是一个int对象...')

@print_obj.register(float)
def _(obj):
    print(f'这是一个float对象...')

@print_obj.register(str)
def _(obj):
    print(f'这是一个字符串对象!')

if __name__ == '__main__':
    print_obj(1)
    print_obj(1.0)
    print_obj('1')
    print_obj(b'1')
```


![](https://img-blog.csdnimg.cn/df2acbdf32af4e04b37624be5c208625.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_17,color_FFFFFF,t_70,g_se,x_16)

print_obj是处理不同参数类型的基函数，通过register注册的专门函数处理专门的参数类型，如果处理不了就会丢给基函数来处理。这样就算有一个新的参数类型来了，只需要为其定义一个专门的处理函数即可！

