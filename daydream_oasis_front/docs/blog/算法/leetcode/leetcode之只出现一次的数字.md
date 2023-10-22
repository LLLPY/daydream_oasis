
<BlogInfo id="1309" title="leetcode之只出现一次的数字" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=61 category="leetcode100题" tag_list="['leetcode', '异或', '动态数组']" create_time="2022.02.05 21:07:35.351077" update_time="2022.07.11 10:36:23" />

## **题目描述**

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]  
输出: 1  
示例 2:

输入: [4,1,2,1,2]  
输出: 4  
通过次数587,015提交次数815,440



## **我的解题思路：**

遍历数组，取当前遍历到的值，调用remove方法两次进行移除该元素，如果成功（说明该数出现了两次），进入下一次循环，此时i的值不变，否则移除当前元素（因为只出现了一次，所以第二次移除时会失败）

## **源码：**
```python
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        while len(nums) > 0:
            try:
                # 首先尝试移除元素两次，如果两次都移除成功，说明要的结果不是当前值，因为当前值被移走了，相当于后面所有
                # 的数都向前挪动了一位，所以i的值不变
                val = nums[i]
                nums.remove(val)
                nums.remove(val)
                # print(f'i={i} 移除了元素{val} nums={nums}')
                i -= 1
            except:  # 如果上面的尝试失败，说明当前值就是只出现了一次的数
                return val
            i += 1
```

## **通过截图：**

![](../media/image/2022/02/05/image-20220205210228-1.png)


内存消耗的排名还不错，但是执行时间太拉跨了，所以我看了一下题解的，大部分都是用的异或操作，首先我查了一下异或的运算规则：

![](../media/image/2022/02/05/image-20220205210416-2.png)

所以按照其运算性质，将数组中的所有元素进行异或运算，最后得到的必是只出现一次的数字，不错，又学到了新东西嘿嘿![](../media/image/2022/02/05/image-20220205210533-3.gif)

源码：

```python
class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        ans = nums[0]

        for i in range(1, len(nums)):

            ans = ans ^ nums[i]

        return ans
```

通过截图：

![](../media/image/2022/02/05/image-20220205210621-4.png)

可以看到，使用异或在执行时间上有明显的优势，但内存消耗比较严重。


























