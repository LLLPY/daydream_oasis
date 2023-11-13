---

next: false

---



<BlogInfo id="5"/>

```python
from sklearn.neighbors import KNeighborsClassifier

# KNN
'''
API:
    sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
    参数:
        n_neighbors:int,默认值为5,默认的邻居数
'''

# 1.构造数据
x = [[0], [1], [100], [200]]  # 必须是二维的
y = [0, 0, 1, 1]  # 对应的标签值(也就是所谓的类别)

# 2.训练模型
# 2.1实例化一个估计器对象
estimator = KNeighborsClassifier(n_neighbors=1)  # k=1
# 2.2调用fit方法,进行训练
estimator.fit(x, y)

# 3.类别预测
# 调用predict方法进行预测
res = estimator.predict([[150]])  # [[150]]二维数据 同上面的x
print(res)

```



<ActionBox />
