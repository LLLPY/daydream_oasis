
<BlogInfo id="1332" title="leetcode之二进制求和" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="57" category="leetcode100题" tag_list="['leetcode', '              十进制', '              二进制']" create_time="2022.02.03 15:10:20.089371" update_time="2022.07.11 10:36:49" />

## **题目描述：**  


''  
给你两个二进制字符串，返回它们的和（用二进制表示）。  
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:  
输入: a = "11", b = "1"  
输出: "100"  
示例 2:

输入: a = "1010", b = "1011"  
输出: "10101"  
提示：

每个字符串仅由字符 '0' 或 '1' 组成。  
1 <= a.length, b.length <= 10^4  
字符串如果不是 "0" ，就都不含前导零。  
'''

## **解法** ：

## 根据十进制转二进制和二进制转十进制的规则分别编写转换函数，其中二进制转十进制可以利用内置函数int进行转换

```python
class Solution:  
    def addBinary(self, a: str, b: str) -> str:

        a_tenth_num = self.binary_to_tenth(a)  
        b_tenth_num = self.binary_to_tenth(b)  
        a_add_b = a_tenth_num + b_tenth_num

        return self.tenth_to_binary(a_add_b)

    # 二进制转十进制  
    def binary_to_tenth(self, binary_num: str) -> int:  
        return int(binary_num,2) #直接使用内置函数int进行转换

       

       #编写自己的转换方法

        # res = 0  
        # k = len(binary_num) - 1  
        # for i in binary_num:  
        #     if i == '1':  
        #         res += pow(2, k)  
        #     k -= 1  
        # return res

    # 十进制转二进制  
    def tenth_to_binary(self, tenth_num: int) -> str:

        # tenth_num:商 remainder：余数 binary_str:结果（二进制）  
        binary_str = f'{tenth_num % 2}'

        while tenth_num > 1:  
            tenth_num = tenth_num // 2  
            # remainder = tenth_num % 2 #节省空间，提交时省略  
            binary_str += f'{tenth_num % 2}'  
            # print(f'余数：{remainder} {binary_str}')

        binary_str_res = ''  
        for i in range(len(binary_str) - 1, -1, -1):  
            binary_str_res += binary_str[i]

        return binary_str_res

if __name__ == '__main__':  
    a = '11'  
    b = '10'  
    print(Solution().addBinary(a, b))

```

最优的一次提交：

![](../media/image/2022/02/03/image-20220203150426-2.png)


