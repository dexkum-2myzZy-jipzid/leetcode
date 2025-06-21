#!/usr/bin/env python3


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 3 children, math
        # a + b + c == n
        # a,b,c <= limit
        # iterate a in [0, limit]:
        # if a = i, b + c == (n-i) and b, c <= limit
        # how many combination b / c

        # n-i-b <= limit -> b >= n-i-limit
        # b <= limit
        # n-i-limit <= b <= limit
        # remove duplicate num

        res = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res
