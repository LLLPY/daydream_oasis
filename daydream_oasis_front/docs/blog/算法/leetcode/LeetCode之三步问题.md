---

next: false

---



<BlogInfo id="1328" title="LeetCode之三步问题" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="45" category="leetcode100题" tag_list="['leetcode', '              dp']" create_time="2022.06.27 19:46:00.652525" update_time="2022.06.27 19:46:00" />

# 题目

>
> 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
>
> 示例1:
>
>  输入：n = 3  
>   输出：4  
>   说明: 有四种走法  
>  示例2:
>
>  输入：n = 5  
>   输出：13
>
> 来源：力扣（LeetCode）  
>  链接：https://leetcode.cn/problems/three-steps-problem-lcci  
>  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

> 和青蛙跳台阶一样，首先写出前几步的结果：
>
> ![](http://www.lll.plus/media/image/2022/06/27/image-20220627194547-2.png)
>
>  通过这些结果，可以发现规律：
>  
>
>     f(n)=f(n-1)+f(n-2)+f(n-3) (n≥3，且f(0)=f(1)=1,f(2)=2)，有了这个规律之后，代码就很好写啦！
>
>
> 也许，有些小伙伴会说，你怎么知道一上来就知道找规律就可以得到正确的结果的？其实我一开始也不知道，就是抱着尝试的态度去的（因为我之前在做"青蛙跳台阶"的时候学到的这个方法，而这个题目和它非常的相似，所以很容易就类比想到这种方法啦！因此，解题的王道：多做，多总结。）

# 源码


```python
class Solution:
    # 类似于只有一次只能爬一阶楼梯或者两阶楼梯，对其进行找规律，发现：f(n)=f(n-1)+f(n-2)+f(n-3) (n≥3，且f(0)=f(1)=1,f(2)=2)
    def waysToStep(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        n0, n1, n2 = 1, 1, 2
        for i in range(n - 2):
            n0, n1, n2 = n1, n2, (n0 + n1 + n2) % 1000000007
            # print(n2)

        return n2
```


# 通过截图

![](https://img-blog.csdnimg.cn/27d48325e1484459b4f3576a5c0740c3.png)







<ActionBox />
