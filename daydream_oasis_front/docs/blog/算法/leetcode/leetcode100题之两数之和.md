---

next: false

---



<BlogInfo id="1324"/>

### "基础不牢,地动山摇",从今天开始,打算在leetcode上进行刷题了~同时将刷题记录在这里,希望对看到的小伙伴也有所帮助~
    
    
'''

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

```python
nums = [2, 7, 11, 15]
target = 9  # 输出：[0,1]


# 方法一:二重循环(时间复杂度(O(n²)))
def solution1():
    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if nums[index1] + nums[index2] and index1 != index2:
                return [index1, index2]


# 方法二:哈希表(时间复杂度:O(n))
'''
用空间换区时间,循环遍历nums列表,依次将当前的数记录在hash表中,用当前数的值作key,当前数的索引作value;
因为如果当前数(num1)加另外一个数(num2)等于target,那么另外一个数始终等于target-num1,所以在对num2
进行查找的时候,直接从hash表中进行查找,这样时间复杂度就降了n维

'''
def solution2():
    hashtable = dict()
    for index, value in enumerate(nums):
        diff = target - value
        if diff in hashtable:
            return [index, hashtable[diff]]
        # 用哈希表记录已访问过的数据
        hashtable[value] = index


if __name__ == '__main__':
    print(solution1())
    print(solution2())

```





<ActionBox />
