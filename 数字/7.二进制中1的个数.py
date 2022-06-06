"""
@Anthor: freya.yang
@Time: 2022/5/10 3:49 下午
@File: 7.二进制中1的个数.py
@description:
"""

def erjinzhi(er):
    print('{:0b}'.format(er))
    return '{:0b}'.format(er).count('1')
    # return '{:0b}'.format(er).count('1')

print(erjinzhi(0b1011))