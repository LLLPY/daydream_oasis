---

next: false

---



<BlogInfo id="772" title="《流畅的python》学习笔记之为什么高手在做增量操作时，不选择tuple，而选择list？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="66" category="《流畅的python》" tag_list="['基础', '              笔记', '              巩固']" create_time="2022.02.14 14:31:09.939869" update_time="2022.07.11 10:43:04" />

### tuple输在了哪里？

平时在用list和tuple做增量操作时，仿佛也察觉不到有啥区别，但是，当数据量变大时？差距是不是就出来？先看一下测试代码：


```python
from time import time

a = [i for i in range(3*10**7)]
b = tuple(a)
print(f'增量操作前a的id={id(a)},b的id={id(b)}')

start=time()
a *= 2
mid=time()
b *= 2
end=time()
print(f'增量操作后a的id={id(a)},b的id={id(b)}')
print(f'列表增量操作耗时：{mid-start}')
print(f'元组增量操作耗时：{end-mid}')
print(f'列表增量的速度时元组增量的{(end-mid)/(mid-start)}')
```

运行结果如下：

![](http://www.lll.plus/media/image/2022/02/14/image-20220214143043-1.png)

可以看到当数据量千万级别时，列表的速度也才是元组的2.2倍左右，虽然这个差距不是很明显，但是，也证明了列表在做增量操作时确实比元组快！那么这其间的原因是什么呢？？

细心的小伙伴可能已经发现，在做增量操作前后，列表a的id是没有发生变化的，而元组b的id却发生了变化！这说明了什么？了解id()函数作用的小伙伴都知道，这说明在元组b进行增量操作的时候
**开辟了新空间，产生了新变量！没错，这就是它慢的原因所在！ "起跑"前得先"搬个家"哈哈哈**


那么这其间的原因究竟是为什么呢？

### **加法增量操作与__add__,__iadd__（就地加法）的关系？**

其实呢，一个序列对象在使用+=操作时，首先会去判断该序列有没有实现__iadd__方法，如果实现了就会去调用该方法，否则，会退而求其次的选择__add__方法。乘法增量中对__imul__和__mul__的调度顺序也是如此！

### **__add__和__iadd__之间的差别**

__iadd__俗称"就地加法"，在进行增量操作时不会产生新的变量，直接将新的值添加在序列的末尾。而__add__就不一样了，假设对序列a进行a+=b的操作。它在操作前，会开辟一个新的地址空间，将其值赋给a，再将a的旧值拷贝到新的地址空间，之后再进行"就地加法"。一句话：
**__add__操作比__iadd__操作更费时！**



### **所以，tuple会输的根本原因是？**

没错，tuple会输的根本原因就是它没有__iadd__方法，只有__add__方法。

tuple仅有的__add__方法

![](https://img-blog.csdnimg.cn/fdfb79ba12dc4f14b80374e51d302b57.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

 list既有__add__方法，也有__iadd__方法

![](https://img-blog.csdnimg.cn/6dde0ded78b44d44bfbd0fb7262f80c1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)



































<ActionBox />
