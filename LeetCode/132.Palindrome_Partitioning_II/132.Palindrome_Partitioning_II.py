#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf
from functools import cache


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        next_idx = [[] for _ in range(n)]

        def is_palindrome(start: int, end: int):
            i, j = start, end
            while 0 <= i and j < n and s[i] == s[j]:
                next_idx[i].append(j + 1)
                i -= 1
                j += 1

        for i in range(n):
            is_palindrome(i, i)
            is_palindrome(i, i + 1)

        # @cache
        # def dfs(i):
        #     if i == n:
        #         return -1

        #     res = inf
        #     for j in next_idx[i]:
        #         res = min(res, dfs(j) + 1)
        #     return res

        # return int(dfs(0))

        dp = [inf] * (n + 1)
        dp[n] = -1

        for i in range(n - 1, -1, -1):
            for end in next_idx[i]:
                dp[i] = min(dp[i], dp[end] + 1)

        return dp[0]
