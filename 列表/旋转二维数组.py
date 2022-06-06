"""
@Anthor: freya.yang
@Time: 2022/4/24 4:50 下午
@File: 旋转二维数组.py
@description:https://www.cnblogs.com/xiximayou/p/14486948.html
"""

ma = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
      ]

# 顺序旋转90度
print(list(zip(*ma[::-1])))  # [(9, 5, 1), (10, 6, 2), (11, 7, 3), (12, 8, 4)]
print(list(map(list, list(zip(*ma[::-1])))))  # [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]

# 逆时针90度
print(list(zip(*[a[::-1] for a in ma])))
# 或者
print(list(zip(*ma))[::-1])

# 顺序打印数组
def ext(maa, lis=[]):
    [lis.extend(i) for i in maa]
    return lis
print(ext(ma))
