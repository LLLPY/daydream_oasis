
<BlogInfo title="LeetCode之剑指 Offer II 091. 粉刷房子，理解这一张图就够了？" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=47 category="leetcode100题" tag_list="['leetcode', '动态规划']" create_time="2022.05.04 00:19:32.490408" update_time="2022.05.04 00:19:32" />

^^^^^^^^^
<h1>题目</h1>

<p>假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。</p>

<p>当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。</p>

<p>例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。</p>

<p>请计算出粉刷完所有房子最少的花费成本。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入: costs = [[17,2,17],[16,16,5],[14,3,19]]<br />
输出: 10<br />
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。<br />
&nbsp;&nbsp; &nbsp; 最少花费: 2 + 5 + 3 = 10。<br />
示例 2：</p>

<p>输入: costs = [[7,6,2]]<br />
输出: 2<br />
&nbsp;</p>

<p>提示:</p>

<p>costs.length == n<br />
costs[i].length == 3<br />
1 &lt;= n &lt;= 100<br />
1 &lt;= costs[i][j] &lt;= 20</p>

<h1>图解</h1>

<p><img src="../media/image/2022/05/04/image-20220504001918-2.png" style="height:523px; width:900px" /></p>

<p>&nbsp;</p>

<h1>&nbsp;源码</h1>

<pre>
# 动态规划求解
class Solution:
    @clocked
    def minCost(self, costs: List[List[int]]) -&gt; int:
        cur_r_min, cur_g_min, cur_b_min = 0, 0, 0  # 第一步
        for r, g, b in costs:
            cur_r_min, cur_g_min, cur_b_min = r + min(cur_g_min, cur_b_min), g + min(cur_r_min, cur_b_min), b + min(cur_r_min, cur_g_min)

            # print(cur_r_min, cur_g_min, cur_b_min)
        return min(cur_r_min, cur_g_min, cur_b_min)</pre>

<p>&nbsp;</p>

<h1>通过截图</h1>

<p><img alt="" data-widget="image" isbindedload="true" src="https://img-blog.csdnimg.cn/1f68e6fb489148a7b86fe0f27e6df857.png" style="height:506px; width:899px" /></p>

<p>&nbsp;</p>

