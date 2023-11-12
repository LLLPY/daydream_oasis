---

next: false

---



<BlogInfo id="782"/>

```python
# 计算n！
def factorial(n) -> int:
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)  # 递给求解


if __name__ == '__main__':
    n = 2
    print(factorial(n))
    print(factorial.__name__)  # 函数名
    print(factorial.__doc__)  # 函数的介绍
    print(factorial.__dict__)
    print(factorial.__slots__)

```



<ActionBox />
