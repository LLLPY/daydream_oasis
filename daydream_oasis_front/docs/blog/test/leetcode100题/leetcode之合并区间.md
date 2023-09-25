
<BlogInfo title="leetcode之合并区间" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=63 category="leetcode100题" tag_list="['leetcode']" create_time="2022.03.28 20:54:23.939442" update_time="2022.07.11 10:33:39" />

^^^^^^^^^
<h2><strong>&nbsp;题目描述：</strong></h2>

<p>以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：intervals = [[1,3],[2,6],[8,10],[15,18]]<br />
输出：[[1,6],[8,10],[15,18]]<br />
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].<br />
示例&nbsp;2：</p>

<p>输入：intervals = [[1,4],[4,5]]<br />
输出：[[1,5]]<br />
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;= intervals.length &lt;= 104<br />
intervals[i].length == 2<br />
0 &lt;= starti &lt;= endi &lt;= 104<br />
通过次数405,696提交次数840,652</p>

<h2><strong>解题思路</strong></h2>

<p>第一步：排序，按照每个区间的第一个值进行排序，保证后面的区间的左值只有两种情况：1.要么大于前面区间的右值，2.或者小于等于前面区间的右值</p>

<p>第二步：遍历排序后的列表，合并有交集的区间，添加独立的区间到结果集中</p>

<p>以intervals = [[1,3],[2,6],[8,10],[15,18]]为例，</p>

<p>首先排序得到：intervals = [[1,3],[2,6],[8,10],[15,18]]</p>

<p>当前区间cur_li=[1,3]</p>

<p>下一个区间[2,6]</p>

<p><img src="../media/image/2022/03/28/image-20220328205340-1.png" style="height:315px; width:900px" /></p>

<p>当发现下一个区间和当前区间不能合并时，直接将当前区间添加到结果集。&nbsp;</p>

<p>&nbsp;</p>

<h2><strong>源码</strong></h2>

<pre>
<code>from typing import List


class Solution:
    flag = 1

    def merge(self, intervals: List[List[int]]) -&gt; List[List[int]]:
        intervals.sort()  # 按第一个数字排序

        intervals_len = len(intervals)
        res_li = []
        i = 0
        while i &lt; intervals_len:
            cur_li = intervals[i] #当前区间
            k = i + 1
            while k &lt; intervals_len:
                cur_ri = intervals[k]  # 当前的区间
                if cur_ri[0] &lt;= cur_li[1]:  # 如果右边区间的左值小于等于左边区间的右值，那么这两个区间可以合并
                    cur_li[1] = max(cur_li[1], cur_ri[1])  # 合并区间
                    i += 1  # 区间被合并，i的值应该加一，向前移动一次
                else:break
                k += 1
            res_li.append(cur_li)  # 加入当前区间（不管该区间有没有合并）

            i += 1
        return res_li</code></pre>

<h2><strong>通过截图：</strong></h2>

<p><img alt="" src="https://img-blog.csdnimg.cn/597334010814426db998811d85085870.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16" style="height:283px; width:900px" /></p>

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

<p>&nbsp;</p>

<p>&nbsp;</p>

