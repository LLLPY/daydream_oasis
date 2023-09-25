
<BlogInfo title="leetcode之汉明距离（一行代码就够了？）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=25 category="leetcode100题" tag_list="['leetcode', '异或']" create_time="2022.03.14 21:18:28.702352" update_time="2022.07.11 10:34:13" />

^^^^^^^^^
<h2>&nbsp;题目描述：</h2>

<p>两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。</p>

<p>给你两个整数 x 和 y，计算并返回它们之间的汉明距离。</p>

<p>示例 1：</p>

<p>输入：x = 1, y = 4<br />
输出：2<br />
解释：<br />
1 &nbsp; (0 0 0 1)<br />
4 &nbsp; (0 1 0 0)<br />
&nbsp; &nbsp; &nbsp; &nbsp;&uarr; &nbsp; &uarr;<br />
上面的箭头指出了对应二进制位不同的位置。<br />
示例 2：</p>

<p>输入：x = 3, y = 1<br />
输出：1</p>

<p>&nbsp;</p>

<h2>解题思路：</h2>

<p>常规思路来应该就是先将这个两个整数分别转成二进制，然后再循环遍历，找相同位但数字不同的位置的个数。</p>

<p>但是仔细想想，相同位置但数字不同？这不正是异或运算干的事吗？</p>

<p>所以，知道异或后，解题应该就很easy了！</p>

<p>看如下源码：</p>

<p>首先通过异或计算出一个结果，然后将其转成二进制，找出二进制中1（因为在异或运算中，如果相同位置的数不相同结果就为1）的个数，就是想要的结果。</p>

<p>&nbsp;</p>

<h2>源码：</h2>

<pre>
<code>class Solution:
    def hammingDistance(self, x: int, y: int) -&gt; int:
        return bin(x ^ y).count(&#39;1&#39;)</code></pre>

<p><img src="../media/image/2022/03/14/image-20220314211823-2.png" style="height:487px; width:905px" /></p>

<p>&nbsp;</p>

