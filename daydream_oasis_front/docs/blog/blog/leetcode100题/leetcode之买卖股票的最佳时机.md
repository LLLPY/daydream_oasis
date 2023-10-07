
<BlogInfo title="leetcode之买卖股票的最佳时机" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=50 category="leetcode100题" tag_list="['leetcode', '动态规划']" create_time="2022.02.07 21:11:59.996867" update_time="2022.07.11 10:35:47" />

^^^^^^^^^
<h2 style="font-style:italic"><strong>题目描述</strong></h2>

<p>给定一个数组 prices ，它的第&nbsp;i 个元素&nbsp;prices[i] 表示一支给定股票第 i 天的价格。</p>

<p>你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>

<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：[7,1,5,3,6,4]<br />
输出：5<br />
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。<br />
&nbsp; &nbsp; &nbsp;注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。<br />
示例 2：</p>

<p>输入：prices = [7,6,4,3,1]<br />
输出：0<br />
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;= prices.length &lt;= 105<br />
0 &lt;= prices[i] &lt;= 104</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>解题思路：</strong></h2>

<p>我一开始用的双指针，但是发现思路行不通，后来想不出来就用了一个双层循环，但可想而知会超时，最后看了题解，感觉顿时就明白了，主要运用到了动态规划。</p>

<p>题解中主要运用到了两个变量</p>

<p>一个当前股价的最小值：这个值的更新方法为很简单，一开始假设其值为列表的第一个元素，之后在遍历列表时，如果当前值小于它，就将当前值赋给它，这样购入最低股票的日期就永远在卖出股票日的前面了</p>

<p>一个是利润的最大值：初始值设为0，在遍历列表的时候，如果当前值-股价最低值大于此时的利润最大值，就将此值更新为该值</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>源码：</strong></h2>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -&gt; int:
        min_price = prices[0]  # 假设第一天的价格最低
        max_profit = 0  # 初始时最大利润设为0
        for cur_p in prices:
            max_profit = max(max_profit, cur_p - min_price) #当前利润=当天的价格-目前最低的价格 用当前利润和最大利润进行比较
            min_price = min(min_price, cur_p) #最低价格也要更新
            # print(f&#39;{cur_p} {min_price} {max_profit}&#39;)

        return max_profit</span></pre>
</div>

<h2 style="font-style:italic"><strong>通过截图：</strong></h2>

<p><img src="../media/image/2022/02/07/image-20220207211155-6.png" style="height:365px; width:926px" /></p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

