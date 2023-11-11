---

next: false

---



<BlogInfo id="1330" title="leetcode之买卖股票的最佳时机" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="50" category="leetcode100题" tag_list="['leetcode', '              动态规划']" create_time="2022.02.07 21:11:59.996867" update_time="2022.07.11 10:35:47" />

## **题目描述**

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。



示例 1：

输入：[7,1,5,3,6,4]  
输出：5  
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。  
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。  
示例 2：

输入：prices = [7,6,4,3,1]  
输出：0  
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。  


提示：

1 <= prices.length <= 105  
0 <= prices[i] <= 104



## **解题思路：**

我一开始用的双指针，但是发现思路行不通，后来想不出来就用了一个双层循环，但可想而知会超时，最后看了题解，感觉顿时就明白了，主要运用到了动态规划。

题解中主要运用到了两个变量

一个当前股价的最小值：这个值的更新方法为很简单，一开始假设其值为列表的第一个元素，之后在遍历列表时，如果当前值小于它，就将当前值赋给它，这样购入最低股票的日期就永远在卖出股票日的前面了

一个是利润的最大值：初始值设为0，在遍历列表的时候，如果当前值-股价最低值大于此时的利润最大值，就将此值更新为该值



## **源码：**
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]  # 假设第一天的价格最低
        max_profit = 0  # 初始时最大利润设为0
        for cur_p in prices:
            max_profit = max(max_profit, cur_p - min_price) #当前利润=当天的价格-目前最低的价格 用当前利润和最大利润进行比较
            min_price = min(min_price, cur_p) #最低价格也要更新
            # print(f'{cur_p} {min_price} {max_profit}')

        return max_profit
```


## **通过截图：**

![](http://www.lll.plus/media/image/2022/02/07/image-20220207211155-6.png)


<ActionBox />
