"""
@Anthor: freya.yang
@Time: 2022/5/10 4:10 下午
@File: 2.2 回文字符串.py
@description:
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

-->
"""
import re

"""
方1：筛选 + 判断
"""
def isHuiwen(strr):
    # temp = [item.lower() for item in filter(str.isalnum, strr)]  -> method1
    temp = "".join(item.lower() for item in strr if item.isalnum())  # --> method2
    return temp == temp[::-1]
#或者
def isHuiwen(strr):
    temp = "".join(item.lower() for item in strr if item.isalnum())
    i, j = 0, len(temp)-1
    while i < j:
        print(i,j)
        if temp[i] != temp[j]:
            return False
        i += 1
        j -= 1
    return True

"""
方2：原字符串上操作
时间复杂度：O(|s|)，其中 |s|是字符串 s的长度。
空间复杂度：O(1)
"""
def isHuiwen2(strr):
    i, j = 0, len(strr)-1
    while i < j:
        if not strr[i].isalnum():
            i = i + 1
        elif not strr[j] .isalnum():
            j = j - 1
        else:
            if strr[i].lower() == strr[j].lower():
                print(strr[i], strr[j])
                i = i + 1
                j = j -1
                print(i, j)
            else:
                return False
    return True

print(isHuiwen('AB.cb.A'))