---

next: false

---



<BlogInfo id="814"/>

```python
# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2022/7/19 8:42
from functools import wraps
from time import time


# 理论上直接从__dict__获取会快一些，因为直接通过键索引 而getattr还要调用一次方法
# 不过测试10000000次两者之间才出现0.1秒的差别，所以它们之间的速度差别不大
class A:

    def __init__(self):
        self.name = 'Tom'


# 计时器
def clocked(func):
    @wraps(func)
    def clock(*args, **kwargs):
        time1 = time()
        res = func(*args, **kwargs)
        time2 = time()
        print(f'cost {time2 - time1}s.')
        return res

    return clock


@clocked
def method_dict_get():
    return [A().__dict__['name'] for i in range(num)]


@clocked
def method_getattr():
    return [getattr(A(), 'name') for i in range(num)]


if __name__ == '__main__':
    num = 10000000
    method_dict_get()
    method_getattr()

```



<ActionBox />
