---

next: false

---



<BlogInfo id="779"/>

### 前言

相信很多小伙伴在对文件操作，或者锁的操作时会经常用到with语句，因为使用它给我们带来了极大的便利，比如在文件操作中，使用它，你再也不用担心你的文件在使用完成后没有关闭；在锁的操作，你也再也不用担心开了一把锁而忘记关闭造成死锁等现象...总之，它会给你做好一切"善后"的事情哈哈哈哈（这个比喻可能不是那么恰当）

### 一、上下文管理器是什么？

上下文管理器对象存在的目的是管理with语句，就像迭代器的存在是为了管理for语句一样。

它包含两个协议：__enter__和__exit__方法。with语句开始时，会在上下文中调用__enter__方法，with语句结束后，会调用__exit__方法。

### 二、使用步骤

这里列出两个实例，两个栗子的目的都是为了在控制中镜像输出。

#### 1.上下文管理器的实现方案一


```python
# 实现一个镜像输出
import sys
class MirrorOutput:

    def __enter__(self):
        self.output = sys.stdout.write  # 定义一个变量用来接受系统的输出方法
        sys.stdout.write = self.__reverse_output__  # 将系统的输出方法改为自己定义的输出方法

    def __reverse_output__(self, text):
        return self.output(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.output  # 退出上下文后将系统的输出方法还原


if __name__ == '__main__':
    with MirrorOutput() as mo:
        print('好好学习，天天向上！')

    print('好好学习，天天向上！')

```

![](http://www.lll.plus/media/image/2022/04/23/image-20220423170732-1.png)


根据with语句的执行步骤，我们只要实现__enter__和__exit__方法，就可以实现一个上下文管理器。

在__enter__中，我们定义一个变量用来保系统的输出方法，同时将系统的输出方法改为我们自己的定义的输出方法(镜像输出)，这样，在with语句内部，只要是在控制台输出的内容，都是镜像的。

在__exit__中，我们将系统的输出方法还原为它原有的方法，保证系统的正确性。在with语句以外的输出方法就是正常的了。


#### 2.上下文管理器的实现方案二

```python
import sys
from contextlib import contextmanager


# 还是实现一个镜像输出
class MirrorOutput:

    @contextmanager
    def mirror_output(self):

        self.output = sys.stdout.write

        def reverse_output(text):
            return self.output(text[::-1])

        sys.stdout.write = reverse_output

        # 分界线以上的作用类似于__enter__方法
        yield "这里是分界线"  # yield产出的值会绑定在as字句的目标变量上
        # 分界线以下的作用类似于__exit__方法
        sys.stdout.write = self.output


if __name__ == '__main__':
    with MirrorOutput().mirror_output() as mo:
        print('好好学习，天天向上！')

        print(mo)
    print('好好学习，天天向上！')
```


![](https://img-blog.csdnimg.cn/8e877eed817c4a80bae007535c8dcd4a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

这里使用了@contextlib.contextmanager装饰器以及yield关键字来实现上下文管理，在yield关键字以上的部分充当__enter__方法，在yield方法以下的部分充当__exit__方法，而yield关键词产出的值会交给as子句后面指定的变量。

### 总结

虽然with语句在我们的代码中频繁会被用到，但是其间的实现过程可能还不是很懂，希望这一文章会在你以后使用with语句时会有所帮助！





<ActionBox />
