"""
@Anthor: freya.yang
@Time: 2022/4/21 1:53 下午
@File: 斐波那契数列
@description:
"""

# 方法一
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for i in fib(10):
    print(i)
print(list(fib(5))[-1])

#方法二
def fib(max):
    if max == 1 or max == 2:
        return 1
    return fib(max-1) + fib(max-2)
print(fib(5))