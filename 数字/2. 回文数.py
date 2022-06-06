"""
@Anthor: freya.yang
@Time: 2022/5/5 11:57 上午
@File: 2. 回文数.py
@description:
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 方法一：双指针
def huiwen1(intt:int) -> bool:
    if intt < 0:
        return False
    else:
        strr = str(intt)
        flag = True
        i , j = 0, len(strr)-1
        while i < j:
            if strr[i] != strr[j]:
                flag = False
                return flag
            else:
                i += 1
                j -= 1
        return flag

# 方法二：切片
def huiwen2(intt : int) -> bool:
    if intt < 0 or str(intt)[-1] == 0:
        return False
    else:
        return str(intt) == str(intt)[::-1]

# 方法三：数字
def huiwen3(intt: int) -> bool:
    if intt < 0 or intt % 10 == 0:
        return False
    else:
        temp = 0
        while intt > temp:
            temp = temp * 10 + intt % 10
            intt //= 10 # 注意：//为向下取整、/为浮点数除法 %为取余
        return intt == temp or intt == temp // 10

print(huiwen1(12321))