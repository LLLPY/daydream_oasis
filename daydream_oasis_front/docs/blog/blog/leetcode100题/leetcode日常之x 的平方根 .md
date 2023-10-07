
<BlogInfo title="leetcode日常之x 的平方根 " author="白日梦想猿" pv=0 read_times=0 pre_cost_time=38 category="leetcode100题" tag_list="['leetcode', '二分法']" create_time="2022.02.04 21:52:46.887883" update_time="2022.07.11 10:37:39" />

^^^^^^^^^
<p><strong>题目描述</strong></p>

<p><br />
&#39;&#39;&#39;<br />
给你一个非负整数 x ，计算并返回&nbsp;x&nbsp;的 算术平方根 。</p>

<p>由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。</p>

<p>注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。</p>

<p>示例 1：</p>

<p>输入：x = 4<br />
输出：2<br />
示例 2：</p>

<p>输入：x = 8<br />
输出：2<br />
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。<br />
&nbsp;<br />
提示：</p>

<p>0 &lt;= x &lt;= 231 - 1<br />
&#39;&#39;&#39;</p>

<p>思路：</p>

<p>题目的大致意思就是：输入一个y，求其的算术平方根x</p>

<p>即y=x&sup2;，求x，其中y为已知的，我的想法是将其转换成一个方程，然后利用算法求其的根（我这里用的是比较简单的二分法求根，因为我只记得这个求根方法了呜呜呜）</p>

<p>假设输入的y已知为a，则得新的方程为：y=x&sup2;-a，求x得值</p>

<p>源码：</p>

<div style="background:#666666; border:1px solid #cccccc; padding:5px 10px">
<p><span style="color:#ffffff">from&nbsp;math&nbsp;import&nbsp;floor</span></p>

<p><span style="color:#ffffff">class&nbsp;Solution:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;def&nbsp;mySqrt(self,&nbsp;y:&nbsp;int)&nbsp;-&gt;&nbsp;int:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.y&nbsp;=&nbsp;y</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;y&nbsp;&lt;&nbsp;4:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;self.half(0,&nbsp;2&nbsp;+&nbsp;1,&nbsp;0.9)</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;误差的取值&nbsp;针对较小的y&nbsp;误差应取较大值&nbsp;针对较大的y&nbsp;误差应取较小值</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k&nbsp;=&nbsp;0.5&nbsp;if&nbsp;y&nbsp;&lt;&nbsp;2&nbsp;**&nbsp;11&nbsp;else&nbsp;0.00006</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;self.half(2,&nbsp;(y&nbsp;/&nbsp;2)&nbsp;+&nbsp;1,&nbsp;k)</span></p>

<p>&nbsp;</p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;定义函数</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;def&nbsp;f(self,&nbsp;x):</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;x&nbsp;**&nbsp;2&nbsp;-&nbsp;self.y</span></p>

<p>&nbsp;</p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;二分法</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;def&nbsp;half(self,&nbsp;a,&nbsp;b,&nbsp;k)&nbsp;-&gt;&nbsp;int:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;=&nbsp;(a&nbsp;+&nbsp;b)&nbsp;/&nbsp;2</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while&nbsp;abs(a&nbsp;-&nbsp;b)&nbsp;&gt;&nbsp;k:</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[a,&nbsp;b]&nbsp;=&nbsp;[a,&nbsp;x]&nbsp;if&nbsp;self.f(x)&nbsp;*&nbsp;self.f(a)&nbsp;&lt;=&nbsp;0&nbsp;else&nbsp;[x,&nbsp;b]</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;=&nbsp;(a&nbsp;+&nbsp;b)&nbsp;/&nbsp;2</span></p>

<p><span style="color:#ffffff">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;floor(x)</span></p>
</div>

<p>&nbsp;</p>

<p>通过截图：</p>

<p><img src="../media/image/2022/02/04/image-20220204215155-1.png" style="height:470px; width:951px" /></p>

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

