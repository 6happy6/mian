"""
@Anthor: freya.yang
@Time: 2022/4/24 3:14 下午
@File: numpy对二维数组的常用操作.py
@description:
"""
import numpy
# lis = [
#     ["a", "aa", "aaa", "aaaa"],
#     ["b", "bb", "bbb", "bbbb"],
#     ["a", "ab", "aba", "abab"],
#     ["a", "aa", "aab", "aabb"]
# ]
#
# lis2 = [
#     [1, 4, 2, 8],
#     [5, 0, 3, 2],
#     [7, 9, 2, 4],
#     [6, 1, 3, 8]
# ]
#
# np_lis = numpy.array(lis)
# np_lis2 = numpy.array(lis2)
#
# # 1、提取二维数组的某几列或某几行
# # print(np_lis[:, [1, 2]])  # 获取第1、3列
# print(np_lis[:, -1])
#
# # 2、获取某个范围的数据
# # print(np_lis[1:3, 1:3])  # 1：3表示左闭右开
#
# # 3、所有元素的求和
# print(np_lis2.sum())
#
# # 4、获取数组的纬度（行数和列数）
# print(np_lis2.shape)
#
# # 5、

ma = [[1,2,3],[4,5,6],[7,8,9]]

npy = numpy.array(ma)
print(npy[1,2])
print(npy[1][2])
# liss = []
# for i in range(npy.shape[1]):
#     liss.append(list(npy[:, i]))
# print(liss)


