#!/usr/bin/env python3


class Solution:
    def soupServings(self, n: int) -> float:
        # Return the probability that soup A will be empty first,
        # plus half the probability that A and B become empty at the same time.

        # dp[(A, B)] = prob
        # if 1th op, dp[(A-100, B-0)] = 0.25 * prob
        # 2-4 do the same
        # res = 0.0
        # if 1th op, A-100 <=0 res += 0.25 * (prob)
        # if A-75 and B-25, res += 0,25 * 0.5 * (prob)

        if n >= 4800:
            return 1.0

        n = (n + 24) // 25
        ops = [(4, 0), (3, 1), (2, 2), (1, 3)]

        @cache
        def dfs(a, b):

            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0

            res = 0.0
            for x, y in ops:
                na, nb = a - x, b - y
                res += 0.25 * (dfs(na, nb))
            return res

        return dfs(n, n)
