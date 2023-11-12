---

next: false

---



<BlogInfo id="567"/>

```python
import numpy as np

# array---深拷贝
# asarray---浅拷贝


# 原始数组a
a = np.array([1, 2, 3, 4, 5, 6])

# 分别通过array和asarray拷贝a数组
print('未修改a[0]=10之前:')
b = np.array(a)
c = np.asarray(a)
print('数组a:', a)
print('数组b:', b)
print('数组c:', c)

# 修改原数组
a[0] = 10
print('在修改a[0]=10后:')
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)

# 修改拷贝得到的数组
b[1] = 1
print('在修改b[0]=1后:')
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)

c[2] = 1
print('原数组a:', a)
print('通过array拷贝数组a得到的数组b:', b)
print('通过asarray拷贝数组a得到的数组c:', c)

# 通过结果可以看到,经过array拷贝的数组b的b[0]值没有发生变化,而通过asarray拷贝的
# 数组c的c[0]的值也随着a[0]的值改变而改变了
# 这种通过asarray方法拷贝得到的数组,因原数组的改变而随之改变的拷贝方法称之为浅拷贝
# 拷贝数组不会因为原数组变化而变化使用的拷贝方法为深拷贝

```



<ActionBox />
