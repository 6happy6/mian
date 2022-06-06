"""
@Anthor: freya.yang
@Time: 2022/5/5 4:22 下午
@File: 5. 删除数组的重复项.py
@description:
"""

def chongfu(lis): # 针对有序数组的去重 [0,0,1,1,1,2,2,3,3,4]
    slow = fast = 1
    while fast < len(lis):
        if lis[fast] != lis[fast -1]:
            lis[slow] = lis[fast]
            slow += 1
        fast += 1
    return slow, lis[:slow]

def chongfu2(lis: list) -> list:
    # return list(set(lis)).sort(key=lambda x: lis.index(x))
    res = sorted(set(lis), key=lis.index)
    return res

lis = [0,0,1,1,1,2,2,3,3,4]
lis2 = [4, 5, 6, 2, 3,3, 2,5]
print(chongfu(lis))
print(chongfu2(lis2))
