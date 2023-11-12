---

next: false

---



<BlogInfo id="760"/>

```python
import re

#search和match的区别

#match是从第一个字符开始匹配，如果第一个字符匹配不成功就会返回None
#search是匹配整个字符串，在整个字符串中进行查找，匹配，如果没有匹配到，才返回None
s = 'I LOVE YOU!'

pattern = 'LOVE'

#使用match进行匹配
x = re.match(pattern,s)
print('使用match进行的匹配:',x)

#使用search进行匹配
x = re.search(pattern,s)
print('使用serach进行ed匹配:',x)
print(type(x.group()))

```



<ActionBox />
