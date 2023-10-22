
<BlogInfo id="1253" title="LeetCode之完全平方数" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=76 category="leetcode100题" tag_list="['leetcode', '动态规划']" create_time="2022.07.13 08:39:20.001563" update_time="2022.07.13 08:39:20" />

# **题目**

>  
>
> **给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。**
>
> **完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
> 不是。**
>
> ** **
>
> **示例  1：**
>
> **输入：n = 12  
>  输出：3  
>  解释：12 = 4 + 4 + 4  
>  示例 2：**
>
> **输入：n = 13  
>  输出：2  
>  解释：13 = 4 + 9  
>  
>  提示：**
>
> **1 <= n <= 104**
>
> **来源：力扣（LeetCode）  
>  链接：https://leetcode.cn/problems/perfect-squares  
>  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。**

# **思路**

> **核心思想还是动态规划，空间换区时间。**
>
> 所以，确定好是动态规划后，我们第一步就先找出动态规划的方程（如下图解）。
>
> ![](https://img-blog.csdnimg.cn/5b30386778d64805b311a7fdd3d40933.png)
>
>  根据如上图解，我们可以进一步细化解题步骤：
>
>   1. 求出n以内的所有完全平方数
>   2. 初始化一个dp数组
>   3. 根据状态转移方程，动态求解每一步的结果
>

>
> ## ![](https://img-blog.csdnimg.cn/98d1374dba5d4e83ae40822bc57edbab.gif)1.求出n以内的所有完全平方数
>

```python
# 求出n之内的所有完全平方数
pow_li = []
for i in range(1, n // 2 + 1):
    cur = i ** 2
    if cur <= n:
        pow_li.append(cur)
    else:
        break
```

>  由n≥1/2时，n²≥n/2,所以只需要遍历到n/2即可。
>
> ## ![](https://img-blog.csdnimg.cn/0d55f4829e4f4da29b02f6e607d384b9.gif)2.初始化一个dp数组
>
>  
>


>  因为1是最小的完全平方数，所以最坏情况就是都是由1这一个完全平方数组成的。
>
> ## ![](https://img-blog.csdnimg.cn/539e319695974b6f9eafa72c129c3ef5.gif)3.根据状态转移方程，动态求解每一步的结果
>
>  
>

```python
 for i in range(2, n + 1):  # 从dp[2]开始
    for tmp in pow_li:
        if i >= tmp:
            dp[i] = min(dp[i - tmp] + 1, dp[i])
        else:
            break
```

>
>  dp[1]=1,所以直接从dp[2]开始，求解dp[i]时，依次遍历完全平方数列表直到找出最小值即可。
>
>  

# 源码


```python
class Solution:
    def numSquares(self, n: int) -> int:

        # 动态规划求解
        '''

        '''

        # 求出n之内的所有完全平方数
        pow_li = []
        for i in range(1, n // 2 + 1):
            cur = i ** 2
            if cur <= n:
                pow_li.append(cur)
            else:
                break
        dp = [i for i in range(n + 1)]  # dp[1]=1
        for i in range(2, n + 1):  # 从dp[2]开始
            for tmp in pow_li:
                if i >= tmp:
                    dp[i] = min(dp[i - tmp] + 1, dp[i])
                else:
                    break
        return dp[n]
```


# 通过截图

![](https://img-blog.csdnimg.cn/4f398da809fb4e7892fedc3cf80bbb9f.png)




