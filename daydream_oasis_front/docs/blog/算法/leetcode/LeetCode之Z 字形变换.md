
<BlogInfo id="1326" title="LeetCode之Z 字形变换" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="141" category="leetcode100题" tag_list="['算法']" create_time="2021.10.19 12:25:59.609179" update_time="2021.10.19 12:32:20" />

  

# **LeetCode,我又回来啦!​**

      

### 久别的LeetCode~

**之前说每天坚持刷一刷LeetCode的算法题的,但是因为种种原因,可能是因为前一段时间真的太忙了挤不出时间了,或者是因为自己的惰性无法坚持下来,所以LeetCode的刷题就被耽搁了,距离上次更新LeetCode的刷题大概已经一个月了,lone time ago~唉,不得不说时间的过得是真的快,虽然说,时间就像海绵里** **的水,只要你肯挤,它总是会有的.但是,很多时候你可能是真的因为事情很多,可能你就用来"挤"的时间都没有,但是,我们也不能因为这些因为外界所致的额外的** **目标不能实现而责备自己!anyway,what done is done,just step forward!所以,多的话不说了,向前看吧,看看自己的未来!**

### 为啥我又回来了?

我想应该有两个原因, **第一:时间比之前稍微充足了一些** ,之前因为忙着做一个物联网的项目,每天除了学校的课程要完成外,其余大部分的时间就花费在它的身上了,但总算是功夫不负有心人,最后还是完成了; **第二:明确了未来的方向:就业!!!** 之前还一直迷惑着:到底是应该考研?还是就业?一开始我的想法是,两个都要准备,主要经历花在考研上,顺便学习编程,但往往想法和现实总是背道而行的,首要,我可以肯定的知道原因在于我自己,举个例子:我可以不吃不喝一整天呆在家里敲代码,但是如果让我连续坐在那里两个小时刷数学题,计算机网络,操作系统啥的,我估计我一个小时都坚持不下去,总之,代码对我的吸引力更大,我对代码的兴趣更浓;虽然一开始我心里就知道了这些,但是总是因为"考研以后发展机会更多...","考研后工资更高...","你们这个专业一定要考研...."等等一些具有"诱惑力"的想法羁绊者,但是,这些不是我内心真的想要的,所以,与其对其念念不忘,不如果断铲除这些念想,坚持自己的初心,坚持自己的心之所向,坚持自己的兴趣,坚持自己想要的东西!所以明确了目标是就业后,现在也已经是大三了,老大不小了,所以现在的目标就是在大三下的时候找到一份自己满意的实习工作,所以现在要为自己将来能找到满意的实习工作而做好准备,刷面经,刷算法题,所以,LeetCode,我又回来啦!!!~  
上面相隔怎么长时间又回来刷LeetCode的一些所感所想吧!希望能对看到的朋友有一些帮助,也希望能够和大家一起学习,一起进步!
下面进入正题了!

先贴上通过的截图,虽然效率不咋地高,但是花了2个多小时把它做出来还是非常的欣慰的!  
![在这里插入图片描述](https://img-blog.csdnimg.cn/1bd03cd3ea0b495098194d66b9b9efbd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)

'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

'''

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows: #如果函数等于1或者字符串的长度小于函数,直接返回原字符串
            return s

        rowList=[]  #初始化第一列到最后一列
        for row in range(numRows):
            rowList.append('')
        #根据numRows确定步长遍历所有元素,并将其添加到属于各自的列中
        groupNum=numRows+(numRows-1)-1

        '''
        1                   .
        2                 .            把这整个看成是一个组group,元素的个数为nomRows+nomRows-1-1
        3                              nomRows:group第一列的元素个数 
        4                              nowRows-1-1:group从第二列到最后一列的元素个数,每一列都只有一个元素
        .           .
        .         .
        .       .
        nomRows                 
        '''

        for i in range(0,len(s),groupNum):
            #将s[i:i+(numRows+numRows-1-1)]的元素看成一个group
            group=s[i:i+groupNum]

            #第一行的元素为group[0]
            rowList[0]+=group[0]
            #最后一行的元素为group[numRows-1]

            if len(group)<groupNum: #如果满足这个条件,说明当前group为最后一个group,它里面的元素个数可能是不足的
                try:
                    rowList[-1] += group[numRows - 1]
                except:pass

                k_le = numRows - 1
                k_ri = numRows - 1
                # 第numRows-1到第二行的元素为:group[k_le],group[k_ri]
                for middleRow in range(numRows - 2, 0, -1):
                    # print(middleRow)
                    k_le -= 1
                    k_ri += 1
                    # print(middleRow,k_le,k_ri)
                    try:
                        rowList[middleRow] += group[k_le]
                    except:pass
                    try:
                        rowList[middleRow] += group[k_ri]
                    except:pass
            else:
                rowList[-1] += group[numRows - 1]

                k_le = numRows - 1
                k_ri = numRows - 1
                # 第numRows-1到第二行的元素为:group[k_le],group[k_ri]
                for middleRow in range(numRows - 2, 0, -1):
                    # print(middleRow)
                    k_le -= 1
                    k_ri += 1
                    # print(middleRow,k_le,k_ri)
                    rowList[middleRow] += (group[k_le]+group[k_ri])

        #依次遍历从第一行到最后一行的元素
        result=''.join(rowList)
        # for row in rowList:
        #     print(rowList.index(row),row)
        return result

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s,numRows))

```

随着numRows的变化,第1到第n行的每行应取的group中元素对应的索引值

![](https://img-blog.csdnimg.cn/171a587650a146a793dfaa2ca792b2a4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbGl0dGxl5Lqu772e,size_20,color_FFFFFF,t_70,g_se,x_16)
根据这个规律来判断每行应该添加的group中的哪些元素,然后记得在最后一个group中,要用到try语句来试探性的取元素,因为最后一个group时,group中的元素可能不是完整的,在使用索引取值时会发生错误.
    


