---

next: false

---



<BlogInfo id="560"/>

```python
import numpy as np
from random import randint
import time

a=[]
for i in range(100000000):
    a.append(randint(0,i))


#通过%time魔法方法,查看当前行代码运行完说花费的时间(jupyter中使用)
%time sum1=sum(a)

b=np.array(a)

%time sum2=np.sum(b)
```



<ActionBox />
