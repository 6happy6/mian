"""
@Anthor: freya.yang
@Time: 2022/4/24 12:17 下午
@File: 输入三个数，排序输出.py
@description:
"""
"""
输入三个整数，按照从小到大顺序输出
"""

a,b,c = map(int, input("请输入三个数，空格分隔").split())
print(a,b,c)
# print(sorted([a,b,c]))

if a > b: a,b=b,a
if a > c: a,c=c,a
if b > c: b,c=c,b
print(a,b,c)