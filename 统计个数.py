"""
@Anthor: freya.yang
@Time: 2022/4/27 5:21 下午
@File: 统计个数.py
@description:
"""
from collections import defaultdict

a = [['yellow', 1], ['blue', 2], ['yellow', 3], ['red', 1]]
b = defaultdict(int)
for k, v in a:
    b[k] += v
print(b)