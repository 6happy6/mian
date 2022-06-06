"""
@Anthor: freya.yang
@Time: 2022/4/20 4:11 下午
@File: 相同字母异序词
@description:
"""

"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1: Input: s = "anagram", t = "nagaram"
Output: true
"""

s = "anagram"
t = "nagaram"

def yixu(s, t):
    ss = sorted(s)
    print(ss)
    tt = sorted(t)
    print(tt)
    print(ss == tt)

yixu(s, t)



