
<BlogInfo id="767" title="python中可迭代的归约函数，功能这么强，你能不爱？ ？ ？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="49" category="《流畅的python》" tag_list="['归约函数']" create_time="2022.04.18 10:14:45.177403" update_time="2022.04.18 10:14:45" />

 相信学习python的小伙伴都用过这些函数，但是它们的功能真的太强了，还是忍不住把它们总结记录一下！！！


```python
import functools
import itertools

# 归约函数:接受一个可迭代对象，然后返回单个结果的函数。

# all(it)
# it中的所有元素都为真时返回True，否者返回False
print(all(range(10)))  # 因为出现了0，所以返回False

# any(it)
# 只有有一个元素是True就返回True，否者返回False
print(any(range(10)))

# max(it,[key=],[default=])
# 返回it中的最大值，key指定排序规则，如果it为空，返回default的值
print(max(['apple', 'banana', 'orange', 'peach'], key=len, default='apple'))  # 按照长度进行比较

# min(it,[key=],[default=])
# 返回it中的最小值，key指定排序规则，如果it为空，返回default的值
print(min([1, 2, -4, -9, 6], key=abs, default=0))  # 按照绝对值进行比较

# itertools.reduce(func,it,[initial])
# 把前两个元素传给func，然后把计算结果和第三个元素传给func，以此类推，返回最后的结果，如果提供了initial
# 就会把它当做第一个元素传入
print(functools.reduce(lambda a, b: a * b, range(1, 11)))  # 计算10！
print(list(itertools.accumulate(range(1, 11), lambda a, b: a * b)))  # 依次计算1! 2! 3!...10!

# sum(it,start=0)
# it中所有元素的总和，如果提供可选的start，会把它加上
print(sum(range(3), start=10))  # 0+1+2+10=13
```


![](http://www.lll.plus/media/image/2022/04/18/image-20220418101439-1.png)

请告诉我，这些函数中哪个你没有用到手软？？？如果有的话，那么证明你对python的爱还是不够哈哈哈哈哈哈

