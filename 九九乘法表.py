"""
@Anthor: freya.yang
@Time: 2022/4/25 1:34 下午
@File: 九九乘法表.py
@description:
"""

for i in range(1, 10):
    temp = []
    for j in range(1, i+1):
        temp.append(f'{j}*{i}={j*i}')
    print(' '.join(temp))
    # print('\n')
