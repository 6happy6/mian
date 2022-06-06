"""
@Anthor: freya.yang
@Time: 2022/5/12 1:18 下午
@File: 8.输入n个数返回k个最小的数.py
@description:
"""

# 3,1,4,2,6,5,7,3,8,1,9
inn = input("请输入多个整数")
print(inn, type(inn))

lis = list(map(int, inn.split(',')))
print(lis)
