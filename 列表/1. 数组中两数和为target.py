"""
@Anthor: freya.yang
@Time: 2022/5/4 3:20 下午
@File: 1. 数组中两数和为target.py
@description:
"""

import time
import datetime

# 方法一（支持重复）
def sum_target(lis, target):
    dic = {}
    res = []
    res_index = []
    for k, v in enumerate(lis):
        dic[v] = k
        if target - v in dic:
            res.append([target-v, v])
            res_index.append([dic[target-v], dic[v]])
    return res, res_index

# 方法二：双指针
def sumtarget2(lis, target):
    print(lis)
    lis2 = sorted(lis)
    i, j = 0, len(lis)-1
    res_index = []
    res = []
    while i < j:
        if lis2[i] + lis2[j] < target:
            i += 1
        elif lis2[i] + lis2[j] > target:
            j -= 1
        else:
            res.append([lis2[i], lis2[j]])
            res_index.append([lis.index(lis2[i]), lis.index(lis2[j])])
            i += 1
            j -= 1
    return res, res_index

# 方法三
def sumtarget2(lis, target):
    res_index = []
    res = []
    for k, v in enumerate(lis):
        temp = target - v
        if temp in lis[k+1:]:
            res.append([v, temp])
            res_index.append([k, lis.index(temp)])
    return res, res_index





if __name__ == '__main__':
    lis = [6, 7, 4, 2, 8, 1, 3, 4]
    start = time.time()
    start2 = datetime.datetime.now()
    print(sum_target(lis, 10))
    print(f"用时：{time.time() - start}")
    print(f"用时：{datetime.datetime.now() - start2}")