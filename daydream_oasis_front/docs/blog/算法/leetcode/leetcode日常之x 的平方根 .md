
<BlogInfo id="1311" title="leetcode日常之x 的平方根 " author="白日梦想猿" pv=0 read_times=0 pre_cost_time=38 category="leetcode100题" tag_list="['leetcode', '二分法']" create_time="2022.02.04 21:52:46.887883" update_time="2022.07.11 10:37:39" />

**题目描述**

  
'''  
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：

输入：x = 4  
输出：2  
示例 2：

输入：x = 8  
输出：2  
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。  
  
提示：

0 <= x <= 231 - 1  
'''

思路：

题目的大致意思就是：输入一个y，求其的算术平方根x

即y=x²，求x，其中y为已知的，我的想法是将其转换成一个方程，然后利用算法求其的根（我这里用的是比较简单的二分法求根，因为我只记得这个求根方法了呜呜呜）

假设输入的y已知为a，则得新的方程为：y=x²-a，求x得值

源码：

```python
from math import floor
class Solution:
    def mySqrt(self, y: int) -> int:
        self.y = y
        if y < 4:
            return self.half(0, 2 + 1, 0.9)
        else:
            # 误差的取值 针对较小的y 误差应取较大值 针对较大的y 误差应取较小值
            k = 0.5 if y < 2 ** 11 else 0.00006
            return self.half(2, (y / 2) + 1, k)
    # 定义函数
    def f(self, x):
        return x ** 2 - self.y
    # 二分法
    def half(self, a, b, k) -> int:
        x = (a + b) / 2
        while abs(a - b) > k:
            [a, b] = [a, x] if self.f(x) * self.f(a) <= 0 else [x, b]
            x = (a + b) / 2
        return floor(x)
```

通过截图：

![](../media/image/2022/02/04/image-20220204215155-1.png)






















































