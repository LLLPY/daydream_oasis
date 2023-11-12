---

next: false

---



<BlogInfo id="991"/>

```python
#过滤数列中的奇数
a = [1,2,3,4,5,6,7,8]

def is_double(n):
    return n % 2 == 0

# True:保留
# False:丢弃
b = filter(is_double,a)
#filter和map一样会作用到序列的每一个数，根据返回值True还是False决定是否保留该数
print(list(b))

#去除序列中的空格
strs = ['12','','  ','hello','  ','世界','',123323,23,34]
#str.strip() :去掉字符串str左右的空格
def not_strip(x):
    return str(x).strip()

#'' : 在进行逻辑运算是，指向False  '  ' :在进行逻辑运算时，指向True

new_strs = filter(not_strip,strs)
print(list(new_strs))
```



<ActionBox />
