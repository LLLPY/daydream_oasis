---

next: false

---



<BlogInfo id="748"/>

```python
import re

s = 'hello world'
pattern = 'hello'
x = re.match(pattern,s)
print(x)
#使用dir()方法可以查看某对象可以使用的方法 使用这些方法的前提:匹配成功
print(dir(x))
#group()返回匹配的字符串
print(x.group())
#span()返回字符串的范围
print(x.span())
#start()返回字符的起始位置
print(x.start())
#如果将pattern里面的h大写,则会匹配不到，这事可以用到match()方法里面的第三个参数flag
pattern2 = 'Hell'
x2 = re.match(pattern2,s,flags=re.I) #flag=re.I代表对不区分大小写
print(x2.group())
```



<ActionBox />
