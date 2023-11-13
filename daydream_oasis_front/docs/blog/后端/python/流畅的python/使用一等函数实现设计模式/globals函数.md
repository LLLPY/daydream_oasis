---

next: false

---



<BlogInfo id="799"/>

```python


#globals函数返回一个字典，表示当前的全局符号表

aaa=[1,2]
bbb=1234
def fun():
    b=globals()
    print(b)
a=globals()
print(a) #在a中可以找到aaa和bbb的值
fun()
```



<ActionBox />
