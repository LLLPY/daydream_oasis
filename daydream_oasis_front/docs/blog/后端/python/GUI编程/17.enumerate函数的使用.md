---

next: false

---



<BlogInfo id="425"/>

```python


''':cvar
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时 列出数据和数据下标 ，一般用在 for 循环当中。

Python 2.3. 以上版本可用，2.6 添加 start 参数
'''

a= ['1','fa','你好','world']
b=enumerate(a)
print(list(b))
for index,i in enumerate(a):
    print(index,':',i)
```



<ActionBox />
