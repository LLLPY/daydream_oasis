# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/4/5 16:47

from collections import OrderedDict

# import scipy.stats
import numpy as np


# 基于物的协同过滤
# 数据预处理
def process_user(user1: dict, user2: dict):
    '''
    对于两个用户的差集，在各自缺的地方补零
    '''

    keys = set()
    user1_keys = set(user1.keys())
    user2_keys = set(user2.keys())
    keys.update(user1_keys)
    keys.update(user2_keys)
    keys = sorted(keys)

    # 使用OrderedDict来保证user1和user2对相同物品的打分是对应的
    sorted_user1 = OrderedDict()
    sorted_user2 = OrderedDict()

    for key in keys:
        sorted_user1[key] = user1.get(key, 0)
        sorted_user2[key] = user2.get(key, 0)

    return sorted_user1, sorted_user2

# 计算用户的余弦相似度
def get_cos_similar(v1: list, v2: list):
    num = float(np.dot(v1, v2))  # 向量点乘
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)  # 求模长的乘积
    # return 0.5 + 0.5 * (num / denom) if denom != 0 else 0
    return (num / denom) if denom != 0 else 0

#计算用户的皮尔孙相似度
# def get_pearsonr_similar(v1: list, v2: list):
#     return scipy.stats.pearsonr(v1, v2)

# 基于用户的协同过滤算法
# @my_cache(timeout=60 * 60)
def cf_user(user, data):
    # 初始化推荐度字典和相似度字典
    recommendation = {}
    similarity_sum = {}

    # 遍历所有用户
    for other_user in data:
        sorted_user1, sorted_user2 = process_user(data.get(user, {}), data[other_user])
        # 如果是当前用户本身，则跳过
        if other_user == user:
            continue

        # 计算当前用户和其他用户的相似度
        similarity = get_cos_similar(list(sorted_user1.values()), list(sorted_user2.values()))

        # 如果相似度为0，则跳过
        if similarity == 0:
            continue

        # 遍历其他用户评过分的物品
        for item in data[other_user]:

            # 如果当前用户已经评过分了该物品，则跳过
            if item in data[user]:
                continue

            # 计算推荐度 其实就是预测user对当前物品的打分 用户之间的相似度*用户的打分
            recommendation.setdefault(item, 0)
            recommendation[item] += data[other_user][item] * similarity

            # 统计相似度之和
            similarity_sum.setdefault(item, 0)
            similarity_sum[item] += similarity

    # 考虑相似用户之间的权重差异将推荐度除以相似度之和，得到最终的推荐度
    for item in recommendation:
        recommendation[item] /= similarity_sum[item]
    return recommendation
    # 对推荐度进行排序
    # return sorted(recommendation.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    # 定义一个字典来保存用户评分数据
    data = {
        'Alice': {'item1': 4, 'item2': 5, 'item3': 2},
        'Bob': {'item1': 3, 'item4': 4, 'item5': 5},
        'Charlie': {'item2': 4, 'item3': 1, 'item5': 3},
        'David': {'item1': 5, 'item3': 3, 'item4': 2},
        'Emma': {'item2': 3, 'item5': 4, 'item6': 4}
    }
    user = 'Alice'

    for user in data:
        result = cf_user(user, data)
        print(result)
        # print(f"为用户{user} 推荐的物品是:")
        # for item, score in result:
        #     print(f"{item}，推荐度: {score:.2f}")
        print('*' * 50)
