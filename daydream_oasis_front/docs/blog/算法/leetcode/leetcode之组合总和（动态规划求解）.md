
<BlogInfo id="1288" title="leetcode之组合总和（动态规划求解）" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=138 category="leetcode100题" tag_list="['leetcode', '动态规划']" create_time="2022.04.18 21:24:11.674157" update_time="2022.04.18 21:24:11" />

#  题目描述：

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的
所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。



示例 1：

输入：candidates = [2,3,6,7], target = 7  
输出：[[2,2,3],[7]]  
解释：  
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。  
7 也是一个候选， 7 = 7 。  
仅有这两种组合。  
示例 2：

输入: candidates = [2,3,5], target = 8  
输出: [[2,2,2,2],[2,3,3],[3,5]]  
示例 3：

输入: candidates = [2], target = 1  
输出: []  


# 解题思路

核心：动态规划， **求解当前的结果时必须建立在之前已经求解的结果之上！**

举个栗子：

![](../media/image/2022/04/18/image-20220418212342-2.png)



已知条件中，有5,4,3,2各拆成两个数字的和，当将5拆成3个数字的和时，5=2+3，我们可以先将2替换成1+1（已有的解）得到一个解，然后再将3换成1+2（已有的解）得到另一个解；将其拆成4个数字的解时原理也是如此...不过要注意的是可能会有重复的，所以可以考虑增加去重的条件。



那么，这个题目的思路也是如此！

以candidates = [2,3,6,7], target = 7为例：

要想知道target=7的解，我们肯定得知道它"前面"的解！那么什么是它"前面"的解呢？为了不遗漏解，我们可以将小于target的所有整数的都看做是它"前面"的解。

比如：

比7小的是6，我们可以先得到6的解集

比6小的是5，我们可以先得到5的解集

...

...

比2小的是1，我们可以先得到1的解集

等于1时，只有一个解[1]

因此，我们可以按照上面的逆序一步一步的求解，只有在得到前一步解的情况下，才能求得现在的解！

每一步的解集我是这样表示的：


```python
# 定义一个字典，用于保存每一步的结果
dic = {i: set() for i in range(1, target + 1)}
```


为什么用集合大家应该都可以猜到：为了去重！


## 每一步的解集怎么得到？

在求解之前，我们可以先将candidates排个序，可以在后面减少遍历的次数！

同时初始化一个candidates的集合。 **（用于查找，效率更高！）**

初始化的结果集为：

![](https://img-blog.csdnimg.cn/a4ba9745a21f48eb8c96f6fcde05b84c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)



计算当前cur_target的结果集：

遍历candidates，假设num为当前遍历得到的结果，进行如下判断：

diff=cur_target-num

if diff<0:当前遍历结束，进入下一个数。

if diff=0:添加一个解集：（num） **以元组的形式添加，因为元组是可hash的！  **然后立马break 进入下一次遍历。

if
diff>0:在candidates_set中查找diff是否存在，如果存在，说明(num,diff)是一个可行解，不过需要将(num,diff)排序后再添加到当前的结果集中（目的是为了去重，结果集中的所有元组中的元素都按从小到大的排序，就不会有重复的了）

之后再到之前的结果集中寻找答案，进行替换。比如：5=2+3，3=1+2=1+1+1此时diff=3，我们就可以将2与3的所有结果集进行组合，此时5得到两个新的解：5=2+（1+2），5=2+（1+1+1）

candidates = [2,3,6,7], target = 7

比如：

求1的解集时：

当遍历到2时，diff=1-2<0,直接结束，所以得到1的解集为()


求2的解集时：

当遍历到2时：diff=2-2=0,添加一个解(2,)，所以得到2的所有解集为((2,))


求3的解集时：

当遍历到2时：diff=3-2=1>0,但是1不在candidates_set中，同时1的解集也为空，所以也无法替换

当遍历到3时：diff=3-3=0，添加一个解(3,),所以得到3的所有解集为((3,))


求4的解集时：

当遍历到2时：diff=4-2=2>0,并且2在candidates_set中，所以得到一个解：(2,2)，然后2的解集为((2,))，遍历2的解集，得到新的解(2,2)，但是已经存在，所以目前还是一个解(2,2)

当遍历到3时：diff=4-3=1>0,但是1不在candidates_set中，并且1的解集也为空()，所以最后得到的4的解集为((2,2),)

...

...

后面的以此类推...

最后就会得到7的解集，也就是我们需要的target的解集！

# 源码：


```python
# 动态规划
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 定义一个字典，用于保存每一步的结果
        dic = {i: set() for i in range(1, target + 1)}
        candidates_set = set(candidates)

        # 将candidates排序
        candidates.sort()
        for cur_target in range(1, target + 1):

            for num in candidates:
                if num <= cur_target:  # 小于目标结果才进行计算
                    diff = cur_target - num  # 目标值减去当前遍历到的值
                    if diff == 0:
                        dic[cur_target].add((num,))  # 说明是自己本身
                        break
                    else:
                        if diff in candidates_set:  # 如果差在candidates中，那么这就是一个解
                            dic[cur_target].add(tuple(sorted((diff, num))))  # 升序排序

                        # 在之前的结果中寻找结果
                        # 可以把diff替换成之前的结果
                        for com in dic[diff]:
                            dic[cur_target].add(tuple(sorted((num, *com))))
                else:
                    break

        return list(dic[target])
```


# 通过截图

![](https://img-blog.csdnimg.cn/9bef3479142c4a8a8efbea615dafb108.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl0dGxl5LquXw==,size_20,color_FFFFFF,t_70,g_se,x_16)






