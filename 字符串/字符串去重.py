
# 1、字符串去重

string = "abcdefacghijkbclm"

# 方法一：
# 注：set()方法对其他数据类型进行转换时往往会遇到顺序被打乱的情况，sort()进行排序，可以保持原顺序
se = sorted(set(string), key=string.index)
print(''.join(se))

# 方法二
res =''
for i in range(len(string)):
    if string[i] not in res:
        res = res + string[i]
print(res)


"""
数组去重
"""

lis = [2, 4, 5, 2, 9, 6, 5, 7,8, 3, 8]
print(list(sorted(set(lis), key=lis.index)))

