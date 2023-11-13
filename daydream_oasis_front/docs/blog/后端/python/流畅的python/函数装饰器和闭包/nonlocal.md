---

next: false

---



<BlogInfo id="803"/>

```python
# nonlocal的作用是把变量标记为自由变量，即使在函数中为变量赋予新指了，也会变成自由变量。


def make_averager():
    total, count = 0, 0

    def avg(num):
        nonlocal total, count
        total += num
        count += 1
        return total / count

    return avg



if __name__ == '__main__':
    avg=make_averager()
    print(avg(1))
    print(avg(2))
    print(avg(3))




```



<ActionBox />
