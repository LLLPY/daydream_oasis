---

next: false

---



<BlogInfo id="562"/>

```python
#导入numpy模块
import numpy as np

#调用array函数创建numpy对象

#创建一维数组
a = np.array([1,2,3]) #第一个参数为列表类型
print(a)
print(np.shape(a)) #
#创建一个二维数组
b = np.array([[1,2,3],[4,5,6],[1111,3333]])
print(b)
print(np.shape(b))
#创建一个三维数组
c = np.array([[[1,2,3],[4,5,6],[1111,3333]]])
print(c)
print(np.shape(c))

#数组中的dtype的使用 它是用来确定数组中每个元素类型的
d = np.array([1,3,4],dtype = float)
print(d)

#数组中ndmin的使用 它使用来确定维度的
e = np.array([1,2],dtype = float , ndmin = 3)
print(e)

```



<ActionBox />
