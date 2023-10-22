
<BlogInfo id="1316" title="leetcode刷题日常" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=143 category="leetcode100题" tag_list="['最大之数组合', '三数之和', '有效单词数']" create_time="2022.01.27 16:30:50.307141" update_time="2022.07.11 10:35:03" />

**[1.句子中的有效单词数](https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/)**  
  
句子仅由小写字母（'a' 到 'z'）、数字（'0' 到 '9'）、连字符（'-'）、标点符号（'!'、'.' 和 ','）以及空格（'
'）组成。每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 ' ' 分隔。  
  
如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：  
  
仅由小写字母、连字符和/或标点（不含数字）。  
至多一个 连字符 '-' 。如果存在，连字符两侧应当都存在小写字母（"a-b" 是一个有效单词，但 "-ab" 和 "ab-" 不是有效单词）。  
至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。  
这里给出几个有效单词的例子："a-b."、"afad"、"ba-c"、"a!" 和 "!" 。  
  
给你一个字符串 sentence ，请你找出并返回 sentence 中 有效单词的数目 。  
  
  
示例 1：  
  
输入：sentence = "cat and  dog"  
输出：3  
解释：句子中的有效单词是 "cat"、"and" 和 "dog"  
示例 2：  
  
输入：sentence = "!this  1-s b8d!"  
输出：0  
解释：句子中没有有效单词  
"!this" 不是有效单词，因为它以一个标点开头  
"1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字  
示例 3：  
  
输入：sentence = "alice and  bob are playing stone-game10"  
输出：5  
解释：句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"  
"stone-game10" 不是有效单词，因为它含有数字  
示例 4：  
  
输入：sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."  
输出：6  
解释：句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."  
  
  
提示：  
  
1 <= sentence.length <= 1000  
sentence 由小写英文字母、数字（0-9）、以及字符（' '、'-'、'!'、'.' 和 ','）组成  
句子中至少有 1 个 token  


我的解题思路：发现其规律，使用正则表达式进行匹配

源码：
```python
from re import match

class Solution:
    def countValidWords(self, sentence: str) -> int:
        # 1.将句子拆分成一个一个的token
        word_list = sentence.split(' ')
        # 2.判断是否满足合格单词的要求
        n = 0
        for word in word_list:
            #存在大写字母，数字，空格的一定不是有效单词
            if word and match(r'[[a-z]*-{0}[a-z]*[!.,]{0,1}$|[a-z]+-{1}[a-z]+[!.,]{0,1}$|[!.,]{0,1}]',word): #去掉空格
                n += 1

        return n
```


![](../media/image/2022/01/27/image-20220127162127-1.png)



## **[2\. 最大子数组和](https://leetcode-cn.com/problems/maximum-subarray/)**

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]  
输出：6  
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。  
示例 2：

输入：nums = [1]  
输出：1  
示例 3：

输入：nums = [5,4,-1,7,8]  
输出：23  


提示：

1 <= nums.length <= 105  
-104 <= nums[i] <= 104  


进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

通过次数829,284提交次数1,502,462

解题思路（参照官方）：动态规划法，只要前面的元素大于0就将其加上

源码：
```python
from typing import List

# 动态规划法，只要前面的元素大于0就将其加上
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)
```


![](../media/image/2022/01/27/image-20220127162448-2.png)

## **[3\. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)**

给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



示例 1：

输入：nums = [-1,2,1,-4], target = 1  
输出：2  
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。  
示例 2：

输入：nums = [0,0,0], target = 1  
输出：0  


提示：

3 <= nums.length <= 1000  
-1000 <= nums[i] <= 1000  
-104 <= target <= 104  
通过次数298,321提交次数650,522

解题思路：双指针法

源码：
```python
# 双指针法（同三数之和）
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        num_length = len(nums)
        nums.sort()  # 排序
        res = nums[0] + nums[1] + nums[2]  # 初始化一个值
        for i in range(num_length):
            num = nums[i]
            left = 0
            right = num_length - 1
            # print(f'num={num} {nums} ')
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                else:
                    num_left = nums[left]
                    num_right = nums[right]
                    cur_res = num + num_left + num_right
                    # print(f'{num_left}  {num}  {num_right}  res={cur_res}')
                    if cur_res == target:
                        return cur_res
                    if abs(cur_res - target) < abs(res - target):
                        res = cur_res
                    # 移动指针
                    if cur_res <= target:
                        left += 1
                    else:
                        right -= 1
        return res
```


![](../media/image/2022/01/27/image-20220127162754-3.png)


今天的收获：对正则和双指针法的复习???








