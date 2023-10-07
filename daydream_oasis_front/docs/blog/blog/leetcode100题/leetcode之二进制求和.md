
<BlogInfo title="leetcode之二进制求和" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=57 category="leetcode100题" tag_list="['leetcode', '十进制', '二进制']" create_time="2022.02.03 15:10:20.089371" update_time="2022.07.11 10:36:49" />

^^^^^^^^^
<h2 style="font-style:italic"><strong>题目描述：</strong><br />
&nbsp;</h2>

<p>&#39;&#39;<br />
给你两个二进制字符串，返回它们的和（用二进制表示）。<br />
输入为 非空 字符串且只包含数字&nbsp;1&nbsp;和&nbsp;0。</p>

<p>示例&nbsp;1:<br />
输入: a = &quot;11&quot;, b = &quot;1&quot;<br />
输出: &quot;100&quot;<br />
示例&nbsp;2:</p>

<p>输入: a = &quot;1010&quot;, b = &quot;1011&quot;<br />
输出: &quot;10101&quot;<br />
提示：</p>

<p>每个字符串仅由字符 &#39;0&#39; 或 &#39;1&#39; 组成。<br />
1 &lt;= a.length, b.length &lt;= 10^4<br />
字符串如果不是 &quot;0&quot; ，就都不含前导零。<br />
&#39;&#39;&#39;</p>

<h2 style="font-style:italic"><strong>解法</strong>：</h2>

<h2 style="font-style:italic">根据十进制转二进制和二进制转十进制的规则分别编写转换函数，其中二进制转十进制可以利用内置函数int进行转换</h2>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<p><span style="color:#ffffff">class Solution:<br />
&nbsp;&nbsp;&nbsp; def addBinary(self, a: str, b: str) -&gt; str:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a_tenth_num = self.binary_to_tenth(a)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b_tenth_num = self.binary_to_tenth(b)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a_add_b = a_tenth_num + b_tenth_num</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return self.tenth_to_binary(a_add_b)</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp; # 二进制转十进制<br />
&nbsp;&nbsp;&nbsp; def binary_to_tenth(self, binary_num: str) -&gt; int:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return int(binary_num,2) #直接使用内置函数int进行转换</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></p>

<p><span style="color:#ffffff">&nbsp; &nbsp; &nbsp; &nbsp;#编写自己的转换方法</span></p>

<p><span style="color:#ffffff">&nbsp; &nbsp; &nbsp; &nbsp; # res = 0<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # k = len(binary_num) - 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # for i in binary_num:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&nbsp;&nbsp;&nbsp;&nbsp; if i == &#39;1&#39;:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; res += pow(2, k)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&nbsp;&nbsp;&nbsp;&nbsp; k -= 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # return res</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp; # 十进制转二进制<br />
&nbsp;&nbsp;&nbsp; def tenth_to_binary(self, tenth_num: int) -&gt; str:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # tenth_num:商 remainder：余数 binary_str:结果（二进制）<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; binary_str = f&#39;{tenth_num % 2}&#39;</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while tenth_num &gt; 1:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; tenth_num = tenth_num // 2<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # remainder = tenth_num % 2 #节省空间，提交时省略<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; binary_str += f&#39;{tenth_num % 2}&#39;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # print(f&#39;余数：{remainder} {binary_str}&#39;)</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; binary_str_res = &#39;&#39;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in range(len(binary_str) - 1, -1, -1):<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; binary_str_res += binary_str[i]</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return binary_str_res</span></p>

<p><span style="color:#ffffff">if __name__ == &#39;__main__&#39;:<br />
&nbsp;&nbsp;&nbsp; a = &#39;11&#39;<br />
&nbsp;&nbsp;&nbsp; b = &#39;10&#39;<br />
&nbsp;&nbsp;&nbsp; print(Solution().addBinary(a, b))</span></p>
</div>
</div>

<p>最优的一次提交：</p>

<p><img src="../media/image/2022/02/03/image-20220203150426-2.png" style="height:700px; width:1031px" />&nbsp;</p>

