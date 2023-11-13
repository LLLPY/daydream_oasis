---

next: false

---



<BlogInfo id="972"/>

```python
"""
语法如下：
for 变量 in 集合：
    循环代码
else：
    没有通过break打破循环，循环结束后，要执行的代码
"""
birthday = ("2001.03.18",)

for birth in birthday:
    print("my birthday is %s"%birth)
    break#当循环被break打破是，else中的代码就不会被执行 
else:
    print("today is 2020.2.12,i have been 19!!!")
```



<ActionBox />
