---

next: false

---



<BlogInfo id="872"/>

```python
# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2022/7/19 9:51
from copy import copy, deepcopy


def say(name):
    print(f'hello,{name}.')


a=[[1,]]
b=copy(a)
b=deepcopy(a)

print(id(a[0]),id(b[0]))
```



<ActionBox />
