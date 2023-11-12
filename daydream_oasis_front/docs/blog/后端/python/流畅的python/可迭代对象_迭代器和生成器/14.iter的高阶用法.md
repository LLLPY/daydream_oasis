---

next: false

---



<BlogInfo id="825"/>

```python
# iter有一个鲜为人知的用法：传入两个参数，使用常规的函数或者任何可调用的的对象
# 创建迭代器。这样使用时，第一个参数必须是可调用的对象，用于不断调用(没有参数)，
# 产出各个值；第二个值是哨符，这个是标记值，当可调用的对象返回这个值时，触发迭代器
# 抛出StopIteration异常，而不产出哨符，程序结束。

from random import randint
def d10():
    return randint(1, 10)


# 随机产生1~10之间的数，遇到5就停止
for i in iter(d10, 5):
    print(i)

# 例： 读取文件，遇到#end\n就结束
# with open('lll07_用于过滤的生成器函数.py', 'r', encoding='utf8') as f:
#     for line in iter(f.readline, '#end\n'):
#         print(line)

```



<ActionBox />
