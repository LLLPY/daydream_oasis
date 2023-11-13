---

next: false

---



<BlogInfo id="981"/>

```python
def powers(x):
    return x*x


#map()函数接受两个参数，一个函数，一个是序列，map将穿传入的函数一次作用到序列的每个元素
list1 = [1,2,3,4,5,6]
list2 = map(powers,list1)
#map函数返回的是一个可迭代的对象

print(list(list2))
```



<ActionBox />
