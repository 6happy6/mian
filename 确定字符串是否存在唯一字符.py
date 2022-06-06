"""
@Anthor: freya.yang
@Time: 2022/4/24 12:32 下午
@File: 1. 确定字符串是否是唯一字符.py
@description:
"""

# def isweiyi(strr):
#     if len(set(strr)) == len(strr):
#         return True
#     else:
#         return False

"""
[
    ["a","aa", "aaa", "aaaa"],
    ["b", "bb", "bbb"],
    ["a", "ab", "aba"],
    ["a", "aa", "aab"]
]

-->
[
    {
        "name": 'aa',
        "child": [
            {
                "name": 'aa',
                "child": [
                    {
                        "name": 'aaa',
                        "child": [
                            ....
                        ]
                    },
                    {
                        "name": 'aab',
                        "child": ....
                    }
                ]
            }
        ]
    }
]
"""



