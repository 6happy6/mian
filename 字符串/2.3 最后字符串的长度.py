"""
@Anthor: freya.yang
@Time: 2022/5/11 2:18 下午
@File: 2.3 最后字符串的长度.py
@description:
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""

# 方1
def getLastLen(strr):
    return len(strr.rsplit(" ", 1)[-1])

# 方2
def getLastLen2(strr):
    i = len(strr)-1
    num = 0
    while i > 0:
        if strr[i] != ' ':
            num += 1
            i -= 1
        else:
            break
    return num


strr = "hello world hei"
print(getLastLen2(strr))