
<BlogInfo title="leetcode之爬楼梯" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=44 category="leetcode100题" tag_list="['leetcode', '阶层']" create_time="2022.02.05 19:55:18.933161" update_time="2022.07.11 10:37:15" />

^^^^^^^^^
<h2 style="font-style:italic"><strong>题目描述</strong></h2>

<p>&nbsp;</p>

<p>假设你正在爬楼梯。需要 n&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：n = 2<br />
输出：2<br />
解释：有两种方法可以爬到楼顶。<br />
1. 1 阶 + 1 阶<br />
2. 2 阶<br />
示例 2：</p>

<p>输入：n = 3<br />
输出：3<br />
解释：有三种方法可以爬到楼顶。<br />
1. 1 阶 + 1 阶 + 1 阶<br />
2. 1 阶 + 2 阶<br />
3. 2 阶 + 1 阶<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;= n &lt;= 45</p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>解题思路：</strong></h2>

<p>根据题意可知：可将题目转化为n=1*x+2*y，求满足条件的x和y，并在满足条件的x和y下将x个1和y个2进行排列组合，求所有的排列组合的和（不准重复），大概就是这个意思。</p>

<p>1.求满足条件的x和y，这个应该没有什么其他的办法，我直接用的双层循环</p>

<p>2.求排列组合，运用排列组合的公式，虽然我忘记了，但是百度到了嘿嘿</p>

<p><img src="../media/image/2022/02/05/image-20220205195339-1.png" style="height:536px; width:1004px" /></p>

<h2 style="font-style:italic"><strong>源码：</strong></h2>

<pre>
class Solution:
    def climbStairs(self, n: int) -&gt; int:
        res = 0
        for x in range(n + 1):
            for y in range(n // 2 + 1):
                if n == x + 2 * y:
                    # print(f&#39;{n}=1*{x}+2*{y}&#39;)
                    if x == 0 or y == 0:
                        res += 1
                    else:
                        n_, m = x + y, min(x, y)
                        #C(n,m)=n!/(m!*(n-m)!)  排列组合
                        res += self.class_(n_) / (self.class_(m) * self.class_(n_ - m))
        return int(res)

    # m的阶层
    def class_(self, m):
        res = 1
        while m &gt; 1:
            res *= m
            m -= 1
        return res


if __name__ == &#39;__main__&#39;:
    print(Solution().climbStairs(5))</pre>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong>通过截图：</strong></h2>

<p><img src="../media/image/2022/02/05/image-20220205195446-2.png" style="height:565px; width:732px" /></p>

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

