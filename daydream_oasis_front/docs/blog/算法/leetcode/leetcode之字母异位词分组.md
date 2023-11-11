---

next: false

---



<BlogInfo id="1339" title="leetcode之字母异位词分组" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="66" category="leetcode100题" tag_list="['leetcode', '              defaultD']" create_time="2022.03.10 23:36:00.414483" update_time="2022.07.11 10:35:25" />

##  题目描述：

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]  
示例 2:

输入: strs = [""]  
输出: [[""]]  
示例 3:

输入: strs = ["a"]  
输出: [["a"]]  


提示：

1 <= strs.length <= 104  
0 <= strs[i].length <= 100  
strs[i] 仅包含小写字母  
通过次数288,834提交次数430,973

## 解题思路：

首先对数组中的每一个字符串进行排序，之后遍历这个列表，做一个映射记录。

这里使用defaultdict，这个强大的字典！！！

它的一个强大的方法就是setdefault(key,default),它的功能如下：

    '''

    返回dict[key]的值，如果有的话，否则返回default，如果有default的话，否则返回None

    在没有dict[key],且传入default的情况下，同时会插入default，即dict[key]=default

    '''

最后得到一个映射的字典数据类型如下：

假设列表中有一个字符串：abc，同时还有acb,bac,bca的字母异位词，那么其在字典中的一个映射就是：abc:[abc,acb,bac,bca]，其他的映射依次类推

最后通过list()方法将映射字典的values()转成列表就得到了想要的结果！

## 源码：


```python
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict=defaultdict() #     {abc:[abc,acb,bac]}
        ordered_list=[''.join(sorted(i)) for i in strs]
        for i in range(len(ordered_list)):
            map_dict.setdefault(ordered_list[i],[]).append(strs[i])
            '''
            返回dict[key]的值，如果有的话，否则返回default，如果有default的话，否则返回None
            在没有dict[key],且传入default的情况下，同时会插入default，即dict[key]=default
    
            '''
        return list(map_dict.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

```


![](http://www.lll.plus/media/image/2022/03/10/image-20220310234152-4.png)

















<ActionBox />
