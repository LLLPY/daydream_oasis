---

next: false

---



<BlogInfo id="1143"/>

```python
# 栈
class Stack():
    def __init__(self, _list=[]):
        self.a = _list

    def push(self, node):  # 入栈
        self.a.append(node)

    def pop(self):  # 出栈
        return self.a.pop()

    def display(self):  # 显示
        return self.a

    def empty(self):  # 是否为空栈
        return not len(self.a)


# 深度优先遍历
def DFS(Graph, root, depth=None) -> list:
    # 遍历深度的确定
    if not depth:
        depth = len(Graph)
    elif depth <= 0:
        depth = 0
    elif depth >= len(Graph):
        depth = len(Graph)
    travelList = [root]  # 记录访问顺序
    travelSet = {root}  # 记录入过栈的节点
    # 定义一个栈对象
    stackTool = Stack()
    # 取出栈顶元素,把与栈顶元素有关系的节点压入栈中
    for i in Graph[root]:
        stackTool.push(i)
        travelSet.add(i)

    while not stackTool.empty():  # 只要栈非空,就一直循环

        if len(travelList) == depth:
            break

        nowNode = stackTool.pop()  # 当前的栈顶元素
        travelList.append(nowNode)  # 访问当前栈顶元素后将其加入用于记录的列表中
        for linkNode in Graph[nowNode]:  # 访问和当前栈顶元素相关的元素
            if linkNode not in travelSet:  # 如果和栈顶元素相关的元素没有入过栈就将其入栈
                stackTool.push(linkNode)
                travelSet.add(linkNode)  # 增加入栈的记录
    return travelList


# 广度优先遍历
def BFS(Graph, root, depth=None) -> list:
    from queue import Queue
    # 遍历深度的确定
    if not depth:
        depth = len(Graph)
    elif depth <= 0:
        depth = 0
    elif depth >= len(Graph):
        depth = len(Graph)

    travelList = [root]  # 记录访问顺序
    travelSet = {root}  # 记录入过队列的节点
    # 定义一个队列对象
    queueTool = Queue()
    # 取出栈队头元素,把与队头元素有关系的节点压入栈中
    for i in Graph[root]:
        queueTool.put(i)
        travelSet.add(i)

    while not queueTool.empty():  # 只要队列非空,就一直循环
        nowNode = queueTool.get()  # 当前的队头元素
        travelList.append(nowNode)  # 访问当前队头元素后将其加入用于记录的列表中
        for linkNode in Graph[nowNode]:  # 访问和当前队头元素相关的元素
            if linkNode not in travelSet:  # 如果和队头元素相关的元素没有入过队列就将其加入队列
                queueTool.put(linkNode)
                travelSet.add(linkNode)  # 增加入队的记录
    return travelList[:depth]


# 朴素贝叶斯
def NaiveBayes(dataList, classSet, testData):
    # 特征值结合
    featureSet = set()
    for feature in list(dataList[0].keys())[:-1]:
        featureSet.add(feature)

    featureCountSet = {}
    for feature in list(dataList[0].keys())[:-1]:
        featureCountSet[feature + '1'] = 0
        featureCountSet[feature + '0'] = 0

    # 计算出数据列表的长度
    dataListLen = len(dataList)

    # 用于各类别出现频数的集合
    classCountSet = {}
    for eachClass in classSet:  # 初始化类别出现频数集合
        classCountSet[eachClass] = 0

    # 计算每一个类别出现的频数
    for eachClass in classSet:
        for data in dataList:
            if data['结果'] == eachClass:
                classCountSet[eachClass] += 1
    print('每一个类别出现的频数:', classCountSet)
    # 计算每一个特征值出现的频数
    for data in dataList:
        for feature in featureSet:
            feature = feature.replace('1', '').replace('0', '')
            if data[feature] == '1':
                featureCountSet[feature + '1'] += 1
            if data[feature] == '0':
                featureCountSet[feature + '0'] += 1

    print('各个特征的特征值出现的次数:', featureCountSet)

    featureUnderClassCountSet = {}
    for feature in featureSet:
        for eachClass in classSet:
            featureUnderClassCountSet[feature + '1_' + eachClass] = 0
            featureUnderClassCountSet[feature + '0_' + eachClass] = 0

    # 计算每一个类别下每一个特征值出现的频数
    for data in dataList:
        for feature in featureSet:
            for eachClass in classSet:
                if data[feature] == '1' and data['结果'] == eachClass:
                    featureUnderClassCountSet[feature + '1_' + eachClass] += 1
                elif data[feature] == '0' and data['结果'] == eachClass:
                    featureUnderClassCountSet[feature + '0_' + eachClass] += 1

    print('每一个类别下每一个特征值出现的频数:', featureUnderClassCountSet)

    # 求各特征取不同特征值下的概率
    probabilityOfEachfeatureSet = {}
    for feature in featureCountSet:
        probabilityOfEachfeatureSet[feature] = featureCountSet[feature] / dataListLen
        probabilityOfEachfeatureSet[feature] = 1 - featureCountSet[feature] / dataListLen
    print('各特征取不同特征值下的概率:', probabilityOfEachfeatureSet)

    probabilityOfEachfeatureUnderClassSet = {}
    # 求各个特征取不同值在不同类别下的概率
    for eachClass in classCountSet:
        for featureUnderClass in featureUnderClassCountSet:
            if featureUnderClass.endswith(str(eachClass)):
                probabilityOfEachfeatureUnderClassSet[f'p({featureUnderClass})'] = featureUnderClassCountSet[
                                                                                       featureUnderClass] / \
                                                                                   classCountSet[eachClass]

    # 计算分母
    denominator = 1
    for test in testData:
        denominator *= probabilityOfEachfeatureSet[test[0] + str(test[1])]

    # print('分母的值:',denominator)
    # 计算分子
    # 计算在不同类下分子的值     # 分别计算需要预测的数据分为不同类别下的概率
    resultList = []
    for eachClass in classSet:
        molecule = 1
        for test in testData:
            molecule *= probabilityOfEachfeatureUnderClassSet[
                'p(' + test[0] + str(test[1]) + '_' + str(eachClass) + ')']
        molecule *= classCountSet[eachClass] / dataListLen  # 分子的最终结果
        result = molecule / denominator
        resultList.append((eachClass, result))
    resultList = sorted(resultList, key=lambda a: a[1], reverse=True)  # 降序排序
    for result in resultList:
        print(f'预测为{classSet[result[0]]}的概率为:{result[1]}.')
    return f'所以预测结果为:{classSet[resultList[0][0]]}'

```



<ActionBox />
