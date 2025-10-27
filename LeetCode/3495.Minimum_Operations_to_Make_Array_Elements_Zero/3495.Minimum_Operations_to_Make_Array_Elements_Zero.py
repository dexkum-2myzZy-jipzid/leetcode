#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import cache


class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:

        # 1 <= l < r <= 109
        # level 1:  1 - 3.  4
        # level 2:  4 - 15. 16-4
        # level 3:  16 - 63. 64 - 16

        @cache
        def helper(i: int) -> int:
            if i == 0:
                return 0

            level, start = 1, 1
            total = 0
            while start <= i:
                r = min(start * 4 - 1, i)
                total += (r - start + 1) * level
                start *= 4
                level += 1

            return total

        res = 0
        for l, r in queries:
            cnt = helper(r) - helper(l - 1)
            mx = helper(r) - helper(r - 1)
            res += max((cnt + 1) // 2, mx)

        return res
