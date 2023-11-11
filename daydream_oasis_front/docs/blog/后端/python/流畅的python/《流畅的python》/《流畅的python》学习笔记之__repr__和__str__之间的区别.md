---

next: false

---



<BlogInfo id="771" title="《流畅的python》学习笔记之__repr__和__str__之间的区别" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="140" category="《流畅的python》" tag_list="['基础', '              笔记', '              巩固']" create_time="2022.02.12 21:05:18.237775" update_time="2022.07.11 10:41:19" />

##  前言

最近开始了新书《流畅的python》一书的学习，在购买此书之前就看了该书的相关简介，主要内容讲的都是python的内置功能，相对而言比较底层一点，因为自己在学习python之初，也是在网上找的视频资料看的，所以基础打的可能不是很牢固，大部分都是只知其然，不知其所以然，所以感觉这本书应该非常适合巩固基础的我。就在刚刚看完了第一章节的内容，感觉整个人都要升华了哈哈哈哈，写的真的太好了！！！！

就真的很多小的细节，作者都讲的很清楚，比如某个内置方法，虽然我在平常经常用到它，但从来没有想过为什么要这样用它，就感觉有一种"本来就是这样的"那种固化思维在这里，看完了第一章，仿佛有了一种"柳暗花明又一村"的那种感jio，就是突然云雾顿开的那种！！！不知道有没有同样经历的小伙伴？这感觉简直不要太爽的哈哈哈哈

![](http://www.lll.plus/media/image/2022/02/12/image-20220212211621-1.gif)


言归正传吧，来看看这俩之间的差别吧！
下面的这种情况你们肯定碰到过！在实例化一个对象后，你直接打印对象，以为可以得到具有表述这个对象的一些特征的东西（比如下面，你定义了一个属性name，就以为会直接输出对象的name的值，可让你意想不到的输出了一串看不懂得东东）
![](https://img-blog.csdnimg.cn/4465de7e7ab842b8b7401f87bc49de75.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)



## **1.字符串表示形式__repr__**

python的有一个内置函数叫repr，它能把一个对象用字符串的形式表达出来以便辨认，这就是"字符串表示形式"。而repr方法就是通过__repr__这个特殊方法（魔法方法）来得到一个对象的字符串表示形式的。

什么时候被调用？

1.交互式控制台用repr函数来获取字符串表示形式。

![](https://img-blog.csdnimg.cn/d4cefbfe518b45fa9db8010cad5db15d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

可以看到，虽然__str__和__repr__函数都定义了，但输出的结果是__repr__函数的。

2.调试程序（debugger）用repr函数来获取字符串表示形式。（这种情况是没用定义__str__函数的，如果定义了__str__就不会调用__repr__了）

![](https://img-blog.csdnimg.cn/3ba959d7e20044689ecc8fd5ab8aaf42.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

可以看到，在把__str__方法注释掉后，在打印对象，或者调用str()方法时，被调用的都是__repr__方法，所以并不是只有__str__在使用print和str方法才会被调用。


## **2.__str__方法**

相较于__repr__方法，这个方法大家应该都比较熟悉，在输出对象或者调用str()方法时，该方法会被调用。这个是大家比较熟悉的定义，但是刚刚在测试的时候发现，在debugger调试程序的时候，如果实现了__str__方法，会优先调用__str__方法（不管有没有实现__repr__方法），如图所示：

![](https://img-blog.csdnimg.cn/886bec4a608b48d4bca3b0112d559d84.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

很明显，在实例化对象后，默认调用的是__str__方法。


## **总结**

__repr__和__str__的区别在于，后者是在str()函数被使用，或者是在用print()函数打印输出时被调用，相较于__repr__方法，__str__返回的字符串对终端用户更友好。

如果只想实现这两个方法中的一个，__repr__是更好的选择，因为在所有没有__str__方法的情况下，__repr__是可以替代它的；而如果在交互式输出对象时，如果就算有__str__方法，但是没有__repr__方法，输出的也还是一串看不懂的地址。


## **其他小知识点（可能是你的知识点盲区哦）**

**1，为啥python能识别加减乘除这样的特殊语法？？？**

答：python解释器碰到特殊的语法时，会使用特殊方法（魔法方法）去激活一些基本的对象操作。

例如：我们熟悉的字典，获取字典中某一个值得写法为:my_dict[key]，当python解释器看到这个语法时，会调用my_dict.__getitem__(key)方法来取值。

在pycharm中，按住ctrl键，鼠标移到中括号那里，可以看到指向了__getitem__方法。

![](https://img-blog.csdnimg.cn/e24a9ce7fc80427f98013ffcbddc11b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 其他对应的：

特殊语法 | 对应的特殊方法  
---|---  
in | __contains__()  
len() | __len__()  
\* | __mul__()  
\+ | __add__()  
bool() | __bool__()  
str() | __str__()  
for | iter()  
  

**2，关于len()方法你不知道的秘密？**

答：在使用len(x)方法获取x的长度时，如果x是python的内置类型（比例list，tuple等），那么len(x)的速度会非常快！背后的原因是Cpyhon会直接从一个C结构体里读取对象的长度，而不是调用__len__方法！所以说，len()方法为python的内置类型开了一个"后门"。


以上就是今天学习的《流畅的python》第一章的大部分的内容了，感觉收货不少！希望也对大家有所帮助！

加油！![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)
![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)
![](https://img-blog.csdnimg.cn/0dc483e5c13a4822a1989290dcb56a44.gif)





<ActionBox />
