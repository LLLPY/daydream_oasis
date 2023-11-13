---

next: false

---



<BlogInfo id="992"/>

```python
from numpy import random

a = list(random.randint(-10,20,(15,)))
a_sort = sorted(a)
print('默认为升序排列:',a_sort)

#逆序排列
b_sort = sorted(a,reverse=True)
print('逆序排列:',b_sort)

#对字符串进行排序
#根据对应的ASCII进行比较
str_list = ['a','bawf','A','G','你好','爱','12']
print(sorted(str_list))

#忽略字符串的大小写进行排序
print(sorted(str_list,key=str.lower)) #str.lower将字符串中的大写字符都小写

```



<ActionBox />
