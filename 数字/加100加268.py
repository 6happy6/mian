"""
@Anthor: freya.yang
@Time: 2022/4/23 5:53 下午
@File: 加100加268.py
@description:
"""
from cmath import sqrt

"""
题目：一个整数，加上100后是个完全平方数，再加上268又是一个完全平方数，请问该数是多少
"""

def pingfang():
    res = []
    for i in range(10000):
        a = int(sqrt(i + 100).real)
        b = int(sqrt(i + 268).real)
        if a ** 2 == (i + 100) and b ** 2 == (i + 268):
            res.append(i)
    return res

print(pingfang())