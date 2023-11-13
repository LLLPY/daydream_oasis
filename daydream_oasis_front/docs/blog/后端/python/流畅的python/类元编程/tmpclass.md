---

next: false

---



<BlogInfo id="873"/>

```python
# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2022/7/19 9:51  

class Say:
    print('执行了类的定义体...')

    def __init__(self, name):
        print('调用了初始化方法...')
        self.name = name

    def say(self):
        print(f'hello,{self.name}')

    class Hello:
        print('hello!')

        class Hi:
            print('Hi!')

```



<ActionBox />
