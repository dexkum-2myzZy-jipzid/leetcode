#!/usr/bin/env python3


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def sideSum(m, l):
            if m - 1 >= l:
                return (m - 1 + m - l) * l // 2
            else:
                return (m - 1 + 1) * (m - 1) // 2 + l - (m - 1)

        lo, hi = 1, maxSum + 1
        res = 1
        while lo < hi:
            mid = (lo + hi) // 2

            total = sideSum(mid, index) + sideSum(mid, n - index - 1) + mid
            if total <= maxSum:
                res = mid
                lo = mid + 1
            else:
                hi = mid

        return res
