
<BlogInfo id="1287" title="else用法的一个小细节" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=23 category="《流畅的python》" tag_list="['小细节', 'else']" create_time="2022.04.23 16:19:00.972018" update_time="2022.04.23 16:21:07" />

###  前言
在python中，大多数情况下，else都是配合if语句使用的，逻辑很简单，如果if的条件满足就执行if中的子句，否者（else）执行else中的。

### 但是偶然也看到配合循环语句使用的else

比如下面这两个栗子：

```python
# 循环只有正常结束才会执行else
for i in range(10):
    print(i)
else:
    print('循环正常结束！')

i = 0
while True:
    print(i)
    i += 1
    if i > 2:
        break
else:
    print('else执行了！')
```

![](../media/image/2022/04/23/image-20220423161836-2.png)

奇怪的是，两个循环都正常执行了，但是第一个执行完成后执行了else语句，而第二个没有！仔细观察的小伙伴可能已经找到差异了：第一个循环没有使用break语句跳出，而第二个使用了！
所以，这个就是else语句的一个小细节： **在配合循环使用时，如果循环没有被break语句打破，循环结束后才会执行else语句。**






