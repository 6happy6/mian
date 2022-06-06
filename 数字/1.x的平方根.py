"""
@Anthor: freya.yang
@Time: 2022/5/15 4:13 下午
@File: 1.x的平方根.py
@description:
"""

# 二分查找：https://www.92python.com/view/314.html
"""
时间复杂度：O(logx)，即为二分查找需要的次数。
空间复杂度：O(1)
"""
class Solution:
    def sqrtt(self, nn: int) -> int:
        left, right, res = 0, nn, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= nn:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

print(Solution().sqrtt(10))