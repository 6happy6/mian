"""
@Anthor: freya.yang
@Time: 2022/5/7 12:46 下午
@File: 6. 爬楼梯.py
@description:
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

"""

def pa(num) -> int:
    if num < 3:
        return num
    a, b = 1, 2
    for i in range(3, num+1):
        a, b = b, a+b
    return b

print(pa(5))