
<BlogInfo title="leetcode刷题日常" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=143 category="leetcode100题" tag_list="['最大之数组合', '三数之和', '有效单词数']" create_time="2022.01.27 16:30:50.307141" update_time="2022.07.11 10:35:03" />

^^^^^^^^^
<p><strong><a href="https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/">1.句子中的有效单词数</a></strong><br />
<br />
句子仅由小写字母（&#39;a&#39; 到 &#39;z&#39;）、数字（&#39;0&#39; 到 &#39;9&#39;）、连字符（&#39;-&#39;）、标点符号（&#39;!&#39;、&#39;.&#39; 和 &#39;,&#39;）以及空格（&#39; &#39;）组成。每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 &#39; &#39; 分隔。<br />
<br />
如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：<br />
<br />
仅由小写字母、连字符和/或标点（不含数字）。<br />
至多一个 连字符 &#39;-&#39; 。如果存在，连字符两侧应当都存在小写字母（&quot;a-b&quot; 是一个有效单词，但 &quot;-ab&quot; 和 &quot;ab-&quot; 不是有效单词）。<br />
至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。<br />
这里给出几个有效单词的例子：&quot;a-b.&quot;、&quot;afad&quot;、&quot;ba-c&quot;、&quot;a!&quot; 和 &quot;!&quot; 。<br />
<br />
给你一个字符串 sentence ，请你找出并返回 sentence 中 有效单词的数目 。<br />
<br />
&nbsp;<br />
示例 1：<br />
<br />
输入：sentence = &quot;cat and &nbsp;dog&quot;<br />
输出：3<br />
解释：句子中的有效单词是 &quot;cat&quot;、&quot;and&quot; 和 &quot;dog&quot;<br />
示例 2：<br />
<br />
输入：sentence = &quot;!this &nbsp;1-s b8d!&quot;<br />
输出：0<br />
解释：句子中没有有效单词<br />
&quot;!this&quot; 不是有效单词，因为它以一个标点开头<br />
&quot;1-s&quot; 和 &quot;b8d&quot; 也不是有效单词，因为它们都包含数字<br />
示例 3：<br />
<br />
输入：sentence = &quot;alice and &nbsp;bob are playing stone-game10&quot;<br />
输出：5<br />
解释：句子中的有效单词是 &quot;alice&quot;、&quot;and&quot;、&quot;bob&quot;、&quot;are&quot; 和 &quot;playing&quot;<br />
&quot;stone-game10&quot; 不是有效单词，因为它含有数字<br />
示例 4：<br />
<br />
输入：sentence = &quot;he bought 2 pencils, 3 erasers, and 1 &nbsp;pencil-sharpener.&quot;<br />
输出：6<br />
解释：句子中的有效单词是 &quot;he&quot;、&quot;bought&quot;、&quot;pencils,&quot;、&quot;erasers,&quot;、&quot;and&quot; 和 &quot;pencil-sharpener.&quot;<br />
&nbsp;<br />
<br />
提示：<br />
<br />
1 &lt;= sentence.length &lt;= 1000<br />
sentence 由小写英文字母、数字（0-9）、以及字符（&#39; &#39;、&#39;-&#39;、&#39;!&#39;、&#39;.&#39; 和 &#39;,&#39;）组成<br />
句子中至少有 1 个 token<br />
&nbsp;</p>

<p>我的解题思路：发现其规律，使用正则表达式进行匹配</p>

<p>源码：</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">from re import match

class Solution:
    def countValidWords(self, sentence: str) -&gt; int:
        # 1.将句子拆分成一个一个的token
        word_list = sentence.split(&#39; &#39;)
        # 2.判断是否满足合格单词的要求
        n = 0
        for word in word_list:
            #存在大写字母，数字，空格的一定不是有效单词
            if word and match(r&#39;[[a-z]*-{0}[a-z]*[!.,]{0,1}$|[a-z]+-{1}[a-z]+[!.,]{0,1}$|[!.,]{0,1}]&#39;,word): #去掉空格
                n += 1

        return n</span></pre>
</div>

<p><img src="../media/image/2022/01/27/image-20220127162127-1.png" style="height:405px; width:900px" /></p>

<p>&nbsp;</p>

<h2 style="font-style:italic"><strong><a href="https://leetcode-cn.com/problems/maximum-subarray/">2. 最大子数组和</a></strong></h2>

<p>给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>

<p>子数组 是数组中的一个连续部分。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：nums = [-2,1,-3,4,-1,2,1,-5,4]<br />
输出：6<br />
解释：连续子数组&nbsp;[4,-1,2,1] 的和最大，为&nbsp;6 。<br />
示例 2：</p>

<p>输入：nums = [1]<br />
输出：1<br />
示例 3：</p>

<p>输入：nums = [5,4,-1,7,8]<br />
输出：23<br />
&nbsp;</p>

<p>提示：</p>

<p>1 &lt;= nums.length &lt;= 105<br />
-104 &lt;= nums[i] &lt;= 104<br />
&nbsp;</p>

<p>进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。</p>

<p>通过次数829,284提交次数1,502,462</p>

<p>解题思路（参照官方）：动态规划法，只要前面的元素大于0就将其加上</p>

<p>源码：</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff">from typing import List

# 动态规划法，只要前面的元素大于0就将其加上
class Solution:
    def maxSubArray(self, nums: List[int]) -&gt; int:

        for i in range(1, len(nums)):
            if nums[i - 1] &gt; 0:
                nums[i] += nums[i - 1]

        return max(nums)</span></pre>
</div>

<p><img src="../media/image/2022/01/27/image-20220127162448-2.png" style="height:452px; width:900px" /></p>

<h2 style="font-style:italic"><strong><a href="https://leetcode-cn.com/problems/3sum-closest/">3. 最接近的三数之和</a></strong></h2>

<p>给你一个长度为 n 的整数数组&nbsp;nums&nbsp;和 一个目标值&nbsp;target。请你从 nums 中选出三个整数，使它们的和与&nbsp;target&nbsp;最接近。</p>

<p>返回这三个数的和。</p>

<p>假定每组输入只存在恰好一个解。</p>

<p>&nbsp;</p>

<p>示例 1：</p>

<p>输入：nums = [-1,2,1,-4], target = 1<br />
输出：2<br />
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。<br />
示例 2：</p>

<p>输入：nums = [0,0,0], target = 1<br />
输出：0<br />
&nbsp;</p>

<p>提示：</p>

<p>3 &lt;= nums.length &lt;= 1000<br />
-1000 &lt;= nums[i] &lt;= 1000<br />
-104 &lt;= target &lt;= 104<br />
通过次数298,321提交次数650,522</p>

<p>解题思路：双指针法</p>

<p>源码：</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<pre>
<span style="color:#ffffff"># 双指针法（同三数之和）
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -&gt; int:
        num_length = len(nums)
        nums.sort()  # 排序
        res = nums[0] + nums[1] + nums[2]  # 初始化一个值
        for i in range(num_length):
            num = nums[i]
            left = 0
            right = num_length - 1
            # print(f&#39;num={num} {nums} &#39;)
            while left &lt; right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                else:
                    num_left = nums[left]
                    num_right = nums[right]
                    cur_res = num + num_left + num_right
                    # print(f&#39;{num_left}  {num}  {num_right}  res={cur_res}&#39;)
                    if cur_res == target:
                        return cur_res
                    if abs(cur_res - target) &lt; abs(res - target):
                        res = cur_res
                    # 移动指针
                    if cur_res &lt;= target:
                        left += 1
                    else:
                        right -= 1
        return res</span>
</pre>
</div>

<p><img src="../media/image/2022/01/27/image-20220127162754-3.png" style="height:451px; width:900px" /></p>

<p>&nbsp;</p>

<p>今天的收获：对正则和双指针法的复习???</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

