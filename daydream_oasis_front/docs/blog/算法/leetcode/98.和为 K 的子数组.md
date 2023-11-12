---

next: false

---



<BlogInfo id="1322"/>

```python
# -*- coding: UTF-8 -*-
'''
   *****************LLL*********************
   * @Project ：leetcode                       
   * @File    ：lll95_和为 K 的子数组.py                  
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/5/15 20:01             
   *****************************************
'''
from typing import List

'''给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 3
    print(Solution().subarraySum(nums, k))

```



<ActionBox />
