---

next: false

---



<BlogInfo id="1325" title="LeetCode100题之整数翻转" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="32" category="leetcode100题" tag_list="['leetcode', '              翻转']" create_time="2021.10.20 15:36:31.011400" update_time="2021.10.20 15:36:31" />

'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        newStr = str(abs(x))[::-1]
        while newStr.startswith('0'):#如果开头为0就去掉
            newStr = newStr[1:]
        intNewStr=int(newStr)
        rangeNum=2**31
        if intNewStr < -rangeNum or intNewStr > rangeNum - 1: #如果反转后整数超过范围,就返回0。
            return 0
        return -intNewStr if x < 0 else intNewStr


if __name__ == '__main__':
    x = -2147483412
    print(Solution().reverse(x))
```
    





<ActionBox />
