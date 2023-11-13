---

next: false

---



<BlogInfo id="844"/>

```python
import itertools

# itertools.count(start,step)
# 用于生成等差数列，起始值为start，步长为step
for i in itertools.count(1, 1):
    print(i)
    break

# itertools.takewhile(predicate,iterable)
# 使用传入的生成器生成另一个生成器，predicate指定终止条件
for i in itertools.takewhile(lambda n: n < 3, range(10)):
    print(i)

```



<ActionBox />
