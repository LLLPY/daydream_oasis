---

next: false

---



<BlogInfo id="806"/>

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



<ActionBox />
