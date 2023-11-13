---

next: false

---



<BlogInfo id="1269"/>

```python
'''
给你两个没有重复元素 的数组nums1和nums2，其中nums1是nums2的子集。
请你找出 nums1中每个元素在nums2中的下一个比其大的值。
nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
'''
from typing import List


# 单调栈实现
class Solution:
    __slots__ = ()

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 维持一个从栈底到栈顶的升序序列
        '''
        因为nums1是nums2的子集，所以直接在nums2中找每一个数下一个最大数即可
        #单调栈的原理：
            只要栈顶元素stack_top小于当前元素cur_num，就将其出栈，并以stack_top:cur_num
            的形式保存在字典中，然后继续比较栈顶元素和当前元素，直到栈为空或者栈顶元素大于当前
            元素，之后将当前元素入栈
        '''
        tmp_dict = {}
        stack = [nums2[0]]
        nums2_len = len(nums2)
        i = 1
        while i < nums2_len:
            cur_num = nums2[i]
            while stack:
                stack_top = stack[-1]
                if stack_top < cur_num:
                    tmp_dict[stack.pop()] = cur_num
                else:
                    break
            stack.append(cur_num)
            i += 1

        res_li = []
        for num1 in nums1:
            res_li.append(tmp_dict.get(num1, -1))
        return res_li


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))

```



<ActionBox />
