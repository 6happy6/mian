"""
@Anthor: freya.yang
@Time: 2022/4/23 6:25 下午
@File: 一年的第几天.py
@description:
"""
"""
输入年月日，返回这是一年的第几天
///须考虑闰年（输入月份大于3时，需考虑多加一天）
ps： 自己写的，待优化，没有考虑闰年
"""
year_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def xday(dat):
    mon, day = int(dat.split('-')[0]), int(dat.split('-')[1])
    # if mon == 1:
    #     return day
    # elif mon > 1:
    #     su = sum([year_dict[k] for k in year_dict.keys() if k < mon]) + day
    #     return su
    # else:
    #     raise
    res = day if mon ==1 else sum([year_dict[k] for k in year_dict.keys() if k < mon]) + day
    return res

print(xday('01-20'))


