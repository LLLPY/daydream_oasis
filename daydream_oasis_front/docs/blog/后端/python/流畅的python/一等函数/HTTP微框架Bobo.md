---

next: false

---



<BlogInfo id="786"/>

```python
#coding:utf8
import bobo

@bobo.query('/')
def hello(person):
    return f'hello {person}'

if __name__ == '__main__':
    print(hello.__code__.co_varnames)

```



<ActionBox />
