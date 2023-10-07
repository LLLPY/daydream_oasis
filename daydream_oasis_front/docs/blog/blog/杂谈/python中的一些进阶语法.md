
<BlogInfo title="python中的一些进阶语法" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=122 category="杂谈" tag_list="['生成器、迭代器', '三元表达式', '推导式']" create_time="2021.11.08 21:06:00" update_time="2021.11.08 21:06:00" />

^^^^^^^^^
<p>&nbsp;&nbsp;&nbsp;&nbsp;最近在csdn上看了一些关于python的进阶语法，感觉写的确实不错，在开发中特别实用，有的虽然很少见，但是功能确实特别强，所以索性自己将其总结了一下，有些自己用的很俗就没有写。</p>

<p>&nbsp;</p>

<p>1.列表推导式</p>

<pre>
#基本格式：[表达式 for 变量 in 旧列表 if 条件]

#携带if
#例：生成100以内除以2余数为0的列表(1到100的偶数列表)
list1=[i for i in range(1,100) if i%2==0]
print(list1)


#携带if..else
#例：1到100，如果为偶数除以2，如果为奇数乘以2，生成新的列表
list2=[i*2 if i%2 else i/2 for i in range(1,100)]
print(list2)</pre>

<p>&nbsp;</p>

<p>2.集合推导式</p>

<pre>
#{}类似于列表推导式，在列表的基础上添加了去除重复项
list3=[i for i in range(1,10)]
set1={x for x in list3}
set1.add(1)
print(set1)</pre>

<p>3.字典推导式</p>

<pre>
dict_demo={
    &#39;a&#39;:1,
    &#39;b&#39;:2,
    &#39;c&#39;:3,
    &#39;d&#39;:4,
    &#39;e&#39;:5,
}

new_dict={ item[1]:item[0] for item in dict_demo.items()}
#dict_demo.items():[(&#39;a&#39;, 1), (&#39;b&#39;, 2), (&#39;c&#39;, 3), (&#39;d&#39;, 4), (&#39;e&#39;, 5)]

print(new_dict)</pre>

<p>&nbsp;</p>

<p>4.生成器</p>

<pre>
# 通过列表生成器，我们可以直接创建一个列表，但是，受到内存限制，列表容量肯定是有限的。并且，我们
# 创建一个包含100万个元素的列表，那后面绝大数元素占用的空间都白白浪费了。所以，如果列表元素可以
# 按照某种算法推到出来，那我们就可以在循环的过程中不断的推出后续的元素，这样就不必创建完整的list，
# 从而节省大量的空间。在python中，这种一边训循环一边计算的机制，称为生成器。

# 得到生成器的方式有两种：1.通过列表推导式得到生成器 2.借助函数完成
# []是列表推导式 ()是生成器
g = (x for x in range(20))
print(type(g), g)
for x in g:
    print(x)


# 只要函数中出现了yield关键字，说明函数就不是函数来，是一个生成器，借助next()得到元素
def func_genexpr():
    n = 0
    while n &lt; 100:
        n += 1
        yield n


g2 = func_genexpr()
print(next(g2))
print(next(g2))
print(next(g2))


# 应用生成器实现斐波那契数列:生成斐波那契数列的前n项
def genexpr_fib(n):
    # 1 1 2 3 5 8
    i = 0
    a, b = 0, 1
    while i &lt; n:
        yield b
        a, b = b, a + b
        i += 1

    # return &#39;没有更多元素了&#39;  # 当while循环执行之后，返回return的值


print(&#39;*&#39; * 50)
g3 = genexpr_fib(10)


while True:
    try:
        print(g3.__next__())
    except:break

# 生成器的应用
# 进程&gt;线程&gt;协程
# 概念：比如迅雷下载1G的视频，叫做进程，然后迅雷将1G的电影按顺序分为10份，这10份叫做线程，然后
# 其中的一份再分为5份，每一份就叫做协程。
def task1(n):
    for i in range(n):
        print(f&#39;正在般第{i}块砖。。。&#39;)
        yield None


def task2(n):
    for i in range(n):
        print(f&#39;正在听第{i}首歌。。。&#39;)
        yield None


g1 = task1(6)
g2 = task2(6)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break</pre>

<p>&nbsp;</p>

<p>5.迭代器</p>

<pre>
#可迭代的对象：生成器 元组 列表 集合 字典 字符串

#迭代器只能往前不能往后，可以被next()函数调用，不断返回下一个值的对象称为迭代器：Iterator
#生成器是可迭代的，并且也是迭代器，列表是可迭代的，但不是迭代器。
#可以通过iter函数将可迭代的对象变成一个迭代器

#判断一个元素是否可迭代
from collections import Iterable
list1=[1,23]
list1_iterable=isinstance(list1,Iterable)
print(list1_iterable)

#将list变成一个迭代器
iter1=iter(list1)
while True:
    try:
        print(iter1.__next__())
    except:break</pre>

<p>&nbsp;</p>

<p>6.三元表达式</p>

<pre>
#格式
#result = 为真时的结果 if 条件 else 为假时的结果
res1=1 if 1==1 else 0
print(res1)

#结合匿名函数的使用
a_list=[1,1,1,1,1]
b_list=[2,2,2,2,2]
c_list=[3,3,3,3,3]
b_res=map(lambda x,y,z:x+y+z if x else x-y-z,a_list,b_list,c_list) #map函数的返回值是一个可迭代的对象
print(list(b_res))
while True:
    try:
        print(b_res.__next__())
    except:break

#三元表达式的一个变种
flag=1
b=[&#39;A&#39;,&#39;B&#39;][bool(flag)] # bool(flag)=True--&gt;1--&gt;[&#39;A&#39;,&#39;B&#39;][1]--&gt;&#39;B&#39;
print(b)</pre>

<p>&nbsp;</p>

<p>7.断言</p>

<pre>
# &ldquo;断言&rdquo;是一个心智正常的检查，确保代码没有做什么明显错误的事情。这些心智正常的检查由assert语句执行，如果检查失败就会
# 抛出异常。
# 格式： assert 条件,当条件失败要执行的语句

# 可以将断言这样理解：我断言这个条件为真，如果不为真，程序中就有一个缺陷(bug)。
# 不像try-except语句，如果assert失败，程序就会崩溃，抛出异常，这样就缩短了你寻找bug的时间
# 断言是针对开发者的，而不是用户

a = 1
assert a == 0, &#39;value error,a!=1&#39;</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
