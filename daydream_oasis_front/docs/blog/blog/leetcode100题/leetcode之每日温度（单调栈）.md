
<BlogInfo title="leetcode之每日温度（单调栈）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=51 category="leetcode100题" tag_list="['leetcode', '单调栈']" create_time="2022.04.16 21:09:37.734063" update_time="2022.04.16 21:29:57" />

^^^^^^^^^
<h2>&nbsp;题目：</h2>

<p>给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。</p>

<p>&nbsp;</p>

<p>示例 1:</p>

<p>输入: temperatures = [73,74,75,71,69,72,76,73]<br />
输出:&nbsp;[1,1,4,2,1,1,0,0]<br />
示例 2:</p>

<p>输入: temperatures = [30,40,50,60]<br />
输出:&nbsp;[1,1,1,0]<br />
示例 3:</p>

<p>输入: temperatures = [30,60,90]<br />
输出: [1,1,0]<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;=&nbsp;temperatures.length &lt;= 105<br />
30 &lt;=&nbsp;temperatures[i]&nbsp;&lt;= 100</p>

<p>&nbsp;</p>

<h2>解题思路：</h2>

<p>1.初始化</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.初始化一个和temperatures一样长的用0填充的列表</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.初始化一个空栈</p>

<p>2.遍历temperatures中每一个元素</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.如果栈为空或者当前温度小于栈顶的温度，就将当前温度的下标入栈</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp; b.如果当前温度大于栈顶温度，说明栈顶温度，说明当天就是栈顶温度的升温日，计算当前温度与栈顶温度的索引差，即可得到栈顶温度升温的天数，将其存入到对应下标的结果列表中</p>

<p>&nbsp; &nbsp; &nbsp; &nbsp;</p>

<h2>代码：</h2>

<pre>
<code>
# 单调栈解法
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -&gt; List[int]:
        stack = []  # 定义一个栈
        temperatures_len = len(temperatures)
        res_li = [0 for i in range(temperatures_len)]  # 初始化结果列表

        for i in range(temperatures_len):
            # 若当日温度大于栈顶温度，说明栈顶元素的升温日已经到了，则将栈顶元素出栈，计算其与当日相差的天数即可
            while stack and temperatures[i] &gt; temperatures[stack[-1]]:
                that_i = stack.pop()  # 栈顶元素的索引值
                days = i - that_i
                res_li[that_i] = days
            else:
                stack.append(i)  # 若栈为空或者当日温度小于等于栈顶温度则直接入栈

        return res_li
</code></pre>

<h2>通过截图：</h2>

<p><img src="../media/image/2022/04/16/image-20220416212937-1.png" style="height:309px; width:900px" /></p>

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

