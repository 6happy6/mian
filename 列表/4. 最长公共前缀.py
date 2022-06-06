"""
@Anthor: freya.yang
@Time: 2022/5/5 1:59 下午
@File: 4. 最长公共前缀.py
@description:
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:

    # sao方法
    def longestprefix(self, lis: list[str]) -> str:
        res = ''
        temp = zip(*lis)
        for i in temp:
            if len(set(i)) == 1:
                res = f'{res}{i[0]}'
            else:
                break
        return res

    def longestprefix2(self, lis: list[str]) -> str:
        temp = lis[0]
        for strr in lis[1:]:
            while not strr.startswith(temp):
                temp = temp[0: len(temp)-1]
        return temp

    # 自己写的笨方法-->有bug，但be长度高于其他的，会报错
    def longestprefix3(self, lis: list) -> str:
        be = lis.pop(0)
        res = ''
        for i in range(len(be)):
            for j in lis:
                if be[i] != j[i]: # 有bug，但be长度高于其他的，会报错
                    break
            else:
                # res += j[i]
                res = f'{res}{j[i]}'
        return ''.join(res)

# lis = ['abbbb', 'abbccc', 'abbbd']
lis = ["flower", "flow", "flight"]
so = Solution()
print(so.longestprefix2(lis))
