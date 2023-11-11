
<BlogInfo id="1331" title="leetcode之二叉树的层序遍历" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="93" category="leetcode100题" tag_list="['leetcode', '              层次遍历']" create_time="2022.05.10 20:35:23.903748" update_time="2022.05.10 20:35:23" />

#  题目

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

![](https://img-blog.csdnimg.cn/img_convert/74ce2ed6e8aa50f7618020662ea58bff.png)​

示例 1：  
输入：root = [3,9,20,null,null,15,7]  
输出：[[3],[9,20],[15,7]]  
示例 2：

输入：root = [1]  
输出：[[1]]  
示例 3：

输入：root = []  
输出：[]

提示：

树中节点数目在范围 [0, 2000] 内  
-1000 <= Node.val <= 1000  
通过次数566,503提交次数875,003

# 思路

相信如果学了队列的小伙伴都知道可以用队列进行层序遍历，但是与常规不一样的地方是，我们学习的时候，所有的层序遍历的结果都是保存在一个列表中，并没有考虑当前结果时那一层？所以这一题的难点就在这里：我怎么知道我当前的节点是在哪一层？

如果是满二叉树的话，我们可以通过数学公式推导出来，但是它不是的！

所以，我们应该换一个思路： **我们可以知道哪些节点是在同一层的！**

比如还是看这个栗子：

![](https://img-blog.csdnimg.cn/img_convert/74ce2ed6e8aa50f7618020662ea58bff.png)​

建立一个队列，从根节点3开始，我们知道它这一层只有一个节点，所以我们只保存一个[3]，同时将3弹出，然后将3的所有孩子节点添加到队列中，然后此时依次弹出队列中的节点（同时用另外一个临时列表保存这些节点，方便后续添加它们的孩子节点到队列中（也就是下一层的所有节点）），将其值依次保留在一个临时数组中，队空后，再将这次的临时结果添加到结果列表中；然后进入下一轮，队列为空时结束。

**手动复现一下：**

![](http://www.lll.plus/media/image/2022/05/10/image-20220510203513-1.png)


# 源码

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from queue import Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 借助队列实现
        '''
        先进先出原则，当访问到某一个节点时，如果它有左孩子，就将左孩子添加到队尾
        如果它有右孩子，就将其添加到队尾，然后将当前节点出队，直到队列为空，遍历结束
        '''
        if not root: return []
        my_queue = Queue()
        my_queue.put(root)  # 从头结点开始
        res_li = []  # 保存结果
        while not my_queue.empty():
            tmp_li = []  # 保存每一层的结果
            cur_node_li = []  # 保存每一层的节点，根据当前节点，方便添加下一层节点
            while not my_queue.empty():
                cur_head = my_queue.get()
                tmp_li.append(cur_head.val)  # 将同一层的节点值保存在tmp_li中
                cur_node_li.append(cur_head)  # 将同一层的节点临时保存在cur_node_li中
            # print(tmp_li)
            res_li.append(tmp_li)
            cur_node_li = cur_node_li[::-1]  # 因为下面用的是pop取值，所以这里将列表翻转一下，保证顺序是正确的
            # 添加当前节点的所有节点到队列中（也就是下一层的节点）
            while cur_node_li:
                cur_head = cur_node_li.pop()
                if cur_head.left:
                    my_queue.put(cur_head.left)
                if cur_head.right:
                    my_queue.put(cur_head.right)
        return res_li
```


# 通过截图

![](https://img-blog.csdnimg.cn/60380468978c4a1191d8666090d8312c.png)


































































