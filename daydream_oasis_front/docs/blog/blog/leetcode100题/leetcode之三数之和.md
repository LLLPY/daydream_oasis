
<BlogInfo title="leetcode之三数之和" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=113 category="leetcode100题" tag_list="['leetcode', '双指针', '降维']" create_time="2022.04.04 21:19:47.595698" update_time="2022.08.22 16:27:41" />

^^^^^^^^^
<h2><strong>&nbsp;题目描述：</strong></h2>

<p>给你一个包含 n 个整数的数组&nbsp;nums，判断&nbsp;nums&nbsp;中是否存在三个元素 a，b，c ，使得&nbsp;a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。</p>

<p>注意：答案中不可以包含重复的三元组。</p>

<p>示例 1：</p>

<p>输入：nums = [-1,0,1,2,-1,-4]<br />
输出：[[-1,-1,2],[-1,0,1]]<br />
示例 2：</p>

<p>输入：nums = []<br />
输出：[]<br />
示例 3：</p>

<p>输入：nums = [0]<br />
输出：[]<br />
&nbsp;</p>

<p>提示：</p>

<p>0 &lt;= nums.length &lt;= 3000<br />
-105 &lt;= nums[i] &lt;= 105</p>

<h2><strong>解题思路：</strong></h2>

<p><strong>核心：降维+双指针法。</strong></p>

<p><strong>1.去重</strong></p>

<p>首先我们可以对数组做初步的处理，三个数字之和等于0，假设这三个数字分别是a，b，c。</p>

<p>a+b+c=0</p>

<p>则所有的组合情况如下：</p>

<p>特殊情况1，三个数字都相等：a=b=c=0</p>

<p>特殊情况2，其中的两个数字相等：a=b=-c,a=c=-b,b=c=-a</p>

<p>一般情况：三个数字都不相同</p>

<p>&nbsp;</p>

<p>所以我们可以断定，不同的数字但值相同（0除外）最多只需要出现2次即可，多余的可以省去。</p>

<p>所以可以去重，降低数据的处理量，相关代码如下：</p>

<pre>
<code># 让一个数最多出现2次,0最多可以出现3次
        num_dic = defaultdict()
        for i in nums:
            cur_li = num_dic.setdefault(i, [])
            if i != 0:
                if len(cur_li) &lt; 2:
                    cur_li.append(i)
            else:
                if len(cur_li) &lt; 3:
                    cur_li.append(i)

        nums = [val for i in num_dic.values() for val in i]</code></pre>

<p><strong>2.排序</strong></p>

<pre>
<code>nums.sort()  # 排序</code></pre>

<p>使用sort()进行排序，不用生成新的数组，减小了开销</p>

<p>&nbsp;</p>

<p><strong>3.降维+双指针寻找解集</strong></p>

<p>可以将三个数字之和看成两个数字和另外一个特殊的数字之和，因为所有的数字都是出自同一个列表，所以这个特殊的数字也一定在这个列表中。</p>

<p>那么可以通过遍历这个数组，假设遍历的得到的值即为这个特殊的数字target，同时使用双指针遍历数组，头指针得到的值为before，尾指针得到的值为after，那么会出现三种情况：</p>

<p>(目的是头指针指向的值+尾指针指向的值+target=0)</p>

<p>1.头指针指向的值+尾指针指向的值&gt;-target：说明两数之和偏大，则尾指针前移</p>

<p>2.头指针指向的值+尾指针指向的值&lt;-target：说明两数之和偏小，则头指针后移</p>

<p>3.头指针指向的值+尾指针指向的值=-target：说明两数之和等于-target，此时头指针后移或者尾指针前移都行，但是一定要移动一个！不能同时移动两个！</p>

<p>如果是第三种情况，再进行如下判断：</p>

<p>如果头指针指向的数字和target不是同一个数字，且尾指针指向的数字和target不是同一个数字，则构成一个解！</p>

<pre>
<code>        for i in range(nums_len):
            before, after = 0, nums_len - 1
            target = nums[i]
            while before != after:
                cur_sum = nums[before] + nums[after]
                if cur_sum &gt; -target:  # 偏大，尾指针前移
                    after -= 1
                elif cur_sum &lt; -target:  # 偏小，头指针后移
                    before += 1
                else:
                    if i != before and i != after:  # 不能是同一个数字
                        res_set.add(tuple(sorted((target, nums[before], nums[after]))))  # 转成元组才能hash，才能作为字典的键
                    before += 1 #after-=1是一样的</code></pre>

<h2><strong>完整代码：</strong></h2>

<pre>
<code>class Solution:
    def threeSum(self, nums: List[int]) -&gt; List[List[int]]:
        if len(nums) &lt; 3:
            return []

        # 降维，遍历数组，遍历到的每一个值设为target，在素组中寻找两个数之和为-target的数
        # 让一个数最多出现2次,0最多可以出现3次
        num_dic = defaultdict()
        for i in nums:
            cur_li = num_dic.setdefault(i, [])
            if i != 0:
                if len(cur_li) &lt; 2:
                    cur_li.append(i)
            else:
                if len(cur_li) &lt; 3:
                    cur_li.append(i)

        nums = [val for i in num_dic.values() for val in i]
        nums.sort()  # 排序
        nums_len = len(nums)
        res_set = set()
        for i in range(nums_len):
            before, after = 0, nums_len - 1
            target = nums[i]
            while before != after:
                cur_sum = nums[before] + nums[after]
                if cur_sum &gt; -target:  # 偏大，尾指针前移
                    after -= 1
                elif cur_sum &lt; -target:  # 偏小，头指针后移
                    before += 1
                else:
                    if i != before and i != after:  # 不能是同一个数字
                        res_set.add(tuple(sorted((target, nums[before], nums[after]))))  # 转成元组才能hash，才能作为字典的键
                    before += 1 #after-=1是一样的
        return [i for i in res_set]</code></pre>

<h2><strong>通过截图：</strong></h2>

<p><img src="../media/image/2022/04/04/image-20220404211934-1.png" style="height:369px; width:900px" /></p>

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

