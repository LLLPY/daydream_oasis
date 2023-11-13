---

next: false

---



<BlogInfo id="570"/>

```python
import numpy as np

a = np.random.randint(60, 100, (40, 50))

# 取其中的一部分进行测试
test = a[10, 0:20]  # 第11行的前20个数
print(test)

# 打印其中大于80的数
print(test[test > 80])

# 将其中大于90的数设为True
test[test > 90] = True
print(test)

```



<ActionBox />
