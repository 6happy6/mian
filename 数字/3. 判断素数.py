"""
@Anthor: freya.yang
@Time: 2022/4/26 8:01 下午
@File: 3. 判断素数.py
@description: https://m.php.cn/article/422194.html
"""
import math
from cmath import sqrt

"""
判断101～200间有多少素数，并输出所有素数
只能被1和其本身整数的数就是素数
"""

# 方一
def sushu(m, n):
    return list(filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x)).real+1) if x%i ==0], range(m,n+1)))
print(sushu(101, 200))

# 方一
def sushu1(start, end):
    num, lis = 0, []
    for i in range(start, end+1):
        for j in range(2, i):
            if i % j ==0:
                break  # 如果 for 循环中有 break 字段等导致 for 循环没有正常执行完毕，那么 else 中的内容也不会执行
        else:
            num += 1
            lis.append(i)
    return num, lis

# 方二：判断素数的方法：一个数分别去除从2到sqrt(这个数)，如果能整除，则不是素数
def sushu2(start, end):
    num, lis = 0, []
    for i in range(start, end+1):
        for j in range(2, int(sqrt(i).real) + 1):
            if i % j == 0:
                break
            else:
                if j == int(sqrt(i).real):
                    num += 1
                    lis.append(i)
                    break
    return num, lis

print(sushu1(101, 201))