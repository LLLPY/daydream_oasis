---

next: false

---



<BlogInfo id="857"/>

```python
# a='a'
# print(f'a对应的unicode码值为：{ord(a)}')


b = (i for i in range(10))


# print(f'{type(b)} {[i for i in b]}')


def add(a, b):
    return a + b

a = [0, 1]
# print(add(*a)) #*a==>0,1


b=[i for i in range(10)]
# print(*b)


for i in range(65535):
    try:
        print(chr(i).encode('utf8').decode('utf8'),end=' ')
    except:
        print(chr(i).encode('utf8').decode('utf8'),end=' ')

    if i%50==0:
        print('\n')

```



<ActionBox />
