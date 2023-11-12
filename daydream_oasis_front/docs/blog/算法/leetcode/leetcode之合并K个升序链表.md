---

next: false

---



<BlogInfo id="1336"/>

# 题目

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。



示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]  
输出：[1,1,2,3,4,4,5,6]  
解释：链表数组如下：  
[  
  1->4->5,  
  1->3->4,  
  2->6  
]  
将它们合并到一个有序链表中得到。  
1->1->2->3->4->4->5->6  
示例 2：

输入：lists = []  
输出：[]  
示例 3：

输入：lists = [[]]  
输出：[]  


提示：

k == lists.length  
0 <= k <= 10^4  
0 <= lists[i].length <= 500  
-10^4 <= lists[i][j] <= 10^4  
lists[i] 按 升序 排列  
lists[i].length 的总和不超过 10^4  
通过次数461,390提交次数811,071

来源：力扣（LeetCode）  
链接：https://leetcode.cn/problems/merge-k-sorted-lists  
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路

感觉这题没啥难的，但是官方设置的标题却是困难。。。

按照常规思路就能写出来，我这里用到的是归并排序，注意，这里给的是链表，所以我写的是对两个链表的归并排序。

我的大概思路就是：遍历链表，每次归并两个链表为一个链表，因此，遍历一次后，需要合并的链表的数量就减半了，直到只剩下一个链表，归并就结束啦！

# 源码


```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return

        while len(lists) > 1:
            tmp_li = []
            if len(lists) % 2: lists.append(None)
            # 如果链表个数是奇数，就添加一个None为辅助链表(放在循环里面的主要原因
            # 是：比如初始链表长度为6，归并一次后长度为3，那么最后一个链表就无法归并)
            for i in range(0, len(lists) - 1, 2):
                cur_li1 = lists[i]
                cur_li2 = lists[i + 1]
                cur_res = self.merge(cur_li1, cur_li2)

                tmp_li.append(cur_res)
                # tmp=[]
                # while cur_res:
                #     tmp.append(cur_res.val)
                #     cur_res = cur_res.next
                # print(tmp)

            lists = tmp_li
        return lists[0]

    # 归并两个链表
    def merge(self, li1, li2):
        li = ListNode()
        head = li
        while li1 and li2:
            cur_val1 = li1.val
            cur_val2 = li2.val

            if cur_val1 <= cur_val2:
                li.next = li1  # 指向li1
                li1 = li1.next  # 指针后移

            else:
                li.next = li2
                li2 = li2.next

            li = li.next

        if li1: li.next = li1
        if li2: li.next = li2

        return head.next


def make_li(li):
    li_node = ListNode(li[0])
    head = li_node
    tmp_li = li[1:]
    tmp_li = tmp_li[::-1]
    while tmp_li:
        li_node.next = ListNode(tmp_li.pop())
        li_node = li_node.next
    return head


if __name__ == '__main__':
    lists = [[-6, -3, -1, 1, 2, 2, 2], [-10, -8, -6, -2, 4], [-2], [-8, -4, -3, -3, -2, -1, 1, 2, 3],
             [-8, -6, -5, -4, -2, -2, 2, 4]]
    li1 = make_li(lists[0])
    li2 = make_li(lists[1])
    li3 = make_li(lists[2])
    li4 = make_li(lists[3])
    li5 = make_li(lists[4])

    lists = [li1, li2, li3, li4, li5]
    res = Solution().mergeKLists(lists)

    res_li = []
    while res:
        res_li.append(res.val)
        res = res.next
    print(res_li)
```


# 提交结果

![](http://www.lll.plus/media/image/2022/05/09/image-20220509204514-4.png)









<ActionBox />
