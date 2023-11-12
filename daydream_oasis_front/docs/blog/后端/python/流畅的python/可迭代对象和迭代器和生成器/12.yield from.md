---

next: false

---



<BlogInfo id="837"/>

```python
# 如果生成器函数需要产出另一个生成器生成的值，传统的方案是使用for循环嵌套

# 例：自己实现chain
def my_chain(*iterable):
    for it in iterable:
        for i in it:
            yield i


# 使用yield from实现
def chain(*iterable):
    for it in iterable:
        yield from it





if __name__ == '__main__':
    it1 = 'ABC'
    it2 = '123'
    print([i for i in my_chain(it1, it2)])
    print([i for i in chain(it1, it2)])

```



<ActionBox />
