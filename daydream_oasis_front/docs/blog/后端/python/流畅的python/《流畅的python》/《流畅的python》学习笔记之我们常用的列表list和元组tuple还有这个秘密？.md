---

next: false

---



<BlogInfo id="778" title="《流畅的python》学习笔记之我们常用的列表list和元组tuple还有这个秘密？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="105" category="《流畅的python》" tag_list="['笔记', '              序列', '              巩固']" create_time="2022.02.13 22:07:51.199276" update_time="2022.07.11 10:41:44" />

### **前言**

不知道大家在学习python中数据类型的时候，在学到tuple和list的区别时，是不是想到的第一句话就是list是可变数据类型，tuple是不可变数据类型，我就猜到了，你想到的肯定是这个嘿嘿

### **可变和不可变序列**

其实这是分类python中序列的一种方法，即可变序列和不可变序列。

#### **python中的可变序列**

```python
list，bytearray，array.array.collections.deque和memoryview

```
##### **python中的不可变序列**

```python
tuple，str和bytes

```
在说另一种分类方法之前，先来看一个神奇的问题???


```python
a = [[]]
b = a * 3
a[0].append('Python')
print(f'添加Python之后的b:{b}')
```

不知道大家有没有猜到答案，正确答案如下：

![](http://www.lll.plus/media/image/2022/02/13/image-20220213220738-1.png)

不知道大家猜到的答案是不是[[], [], []]或者[['Python'], [],[]]或者其他答案？明明是列表a添加了"python"，关我列表b毛事哈哈哈???

但是为啥是上面这个答案呢？？？![](https://img-blog.csdnimg.cn/b8cbd1c95cc145bfb5b5a35eb94c80d8.gif)

 这就要谈到python中序列的另一种分类方式了！

### **容器序列和扁平序列**

python中的容器序列包含：list，tuple和collections.deque

python中的扁平序列包含：str，bytes，bytearray，memoryview，=和array.array

按照这个分类来，你们有没有发现容器序列中，它们存放的元素的类型可以是不同的，比如在同一个list中，既可以存放str，tuple，也可以存放int；但是在扁平容序列中，存放的元素类型必须是一致的，str就就必须全是字符型，bytes就必须全是自字节型。

说到这里，不知道大家有没有想到答案？ **其实能容器序列之所以能够存储不同类型的元素，是因为它存储的不是元素本身，而是对元素的引用，存储的是元素的地址！**
说到这里，想必大家都云雾顿开了吧！！！（配个图也许更清楚一些）

![](https://img-blog.csdnimg.cn/c02791ed7d054c25b0662c5001428e6e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)


### **其他小知识点（可能是你的知识点盲区哦）**

**1.你知道python中如何获取一个字符对应的unicode编码吗？**

答案就是ord()函数：

![](https://img-blog.csdnimg.cn/435a1aa749f24803bd8006c8e2fac76a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_17,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/8bb245d4436c4c4a8a28e07a40c53f2b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_19,color_FFFFFF,t_70,g_se,x_16)

2.你知道最简的生成器表达式吗？

答案就是小括号！

![](https://img-blog.csdnimg.cn/9e3dddd3c6094227b79348ba49cc4b66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

  **3.你知道*除了看作是乘法外，却不知道它还有拆包的作用吗？**

![](https://img-blog.csdnimg.cn/176c9814402c4c39bf408e9719f8d2b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

**  4.假设s是一个序列，对s进行的s[a:b:c]切片含义你知道吗？**

答：在a，b以间隔为c进行取值。

![](https://img-blog.csdnimg.cn/f0f8089883824a3caadd94dc7e6b082b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)


以上就是今天学习的《流畅的python》第二章的前半部分的内容了，感觉收货不少！希望也对大家有所帮助！

加油！
![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)
![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)
![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)



















<ActionBox />
