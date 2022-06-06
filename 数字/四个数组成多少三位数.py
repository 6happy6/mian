"""
@Anthor: freya.yang
@Time: 2022/4/23 5:41 下午
@File: 四个数组成多少三位数.py
@description:
"""

"""
题目：1、2、3、4能组成多少互不相同且无重复数字的三位数？都是多少？
"""

def zuhe(lis):
    res = []
    for i in lis:
        for j in lis:
            for k in lis:
                if i !=j and j !=k and k != i:
                    res.append(int(f'{i}{j}{k}'))
    return res

lis = [1, 2, 3, 4]
print(zuhe(lis))