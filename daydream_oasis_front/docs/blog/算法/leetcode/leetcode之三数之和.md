
<BlogInfo id="1296" title="leetcode之三数之和" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=113 category="leetcode100题" tag_list="['leetcode', '双指针', '降维']" create_time="2022.04.04 21:19:47.595698" update_time="2022.08.22 16:27:41" />

## **  题目描述：**

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]  
输出：[[-1,-1,2],[-1,0,1]]  
示例 2：

输入：nums = []  
输出：[]  
示例 3：

输入：nums = [0]  
输出：[]  


提示：

0 <= nums.length <= 3000  
-105 <= nums[i] <= 105

## **解题思路：**

**核心：降维+双指针法。**

**1.去重**

首先我们可以对数组做初步的处理，三个数字之和等于0，假设这三个数字分别是a，b，c。

a+b+c=0

则所有的组合情况如下：

特殊情况1，三个数字都相等：a=b=c=0

特殊情况2，其中的两个数字相等：a=b=-c,a=c=-b,b=c=-a

一般情况：三个数字都不相同



所以我们可以断定，不同的数字但值相同（0除外）最多只需要出现2次即可，多余的可以省去。

所以可以去重，降低数据的处理量，相关代码如下：


```python
# 让一个数最多出现2次,0最多可以出现3次
num_dic = defaultdict()
for i in nums:
    cur_li = num_dic.setdefault(i, [])
    if i != 0:
        if len(cur_li) < 2:
            cur_li.append(i)
    else:
        if len(cur_li) < 3:
            cur_li.append(i)

nums = [val for i in num_dic.values() for val in i]
```


**2.排序**


```python
nums.sort()  # 排序
```
使用sort()进行排序，不用生成新的数组，减小了开销


**3.降维+双指针寻找解集**

可以将三个数字之和看成两个数字和另外一个特殊的数字之和，因为所有的数字都是出自同一个列表，所以这个特殊的数字也一定在这个列表中。

那么可以通过遍历这个数组，假设遍历的得到的值即为这个特殊的数字target，同时使用双指针遍历数组，头指针得到的值为before，尾指针得到的值为after，那么会出现三种情况：

(目的是头指针指向的值+尾指针指向的值+target=0)

1.头指针指向的值+尾指针指向的值>-target：说明两数之和偏大，则尾指针前移

2.头指针指向的值+尾指针指向的值<-target：说明两数之和偏小，则头指针后移

3.头指针指向的值+尾指针指向的值=-target：说明两数之和等于-target，此时头指针后移或者尾指针前移都行，但是一定要移动一个！不能同时移动两个！

如果是第三种情况，再进行如下判断：

如果头指针指向的数字和target不是同一个数字，且尾指针指向的数字和target不是同一个数字，则构成一个解！


```python
for i in range(nums_len):
    before, after = 0, nums_len - 1
    target = nums[i]
    while before != after:
        cur_sum = nums[before] + nums[after]
        if cur_sum > -target:  # 偏大，尾指针前移
            after -= 1
        elif cur_sum < -target:  # 偏小，头指针后移
            before += 1
        else:
            if i != before and i != after:  # 不能是同一个数字
                res_set.add(tuple(sorted((target, nums[before], nums[after]))))  # 转成元组才能hash，才能作为字典的键
            before += 1 #after-=1是一样的
```


## **完整代码：**


```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # 降维，遍历数组，遍历到的每一个值设为target，在素组中寻找两个数之和为-target的数
        # 让一个数最多出现2次,0最多可以出现3次
        num_dic = defaultdict()
        for i in nums:
            cur_li = num_dic.setdefault(i, [])
            if i != 0:
                if len(cur_li) < 2:
                    cur_li.append(i)
            else:
                if len(cur_li) < 3:
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
                if cur_sum > -target:  # 偏大，尾指针前移
                    after -= 1
                elif cur_sum < -target:  # 偏小，头指针后移
                    before += 1
                else:
                    if i != before and i != after:  # 不能是同一个数字
                        res_set.add(tuple(sorted((target, nums[before], nums[after]))))  # 转成元组才能hash，才能作为字典的键
                    before += 1 #after-=1是一样的
        return [i for i in res_set]
```

## **通过截图：**
![](../media/image/2022/04/04/image-20220404211934-1.png)












































