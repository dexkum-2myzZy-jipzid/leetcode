#!/usr/bin/env python3


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # 3 non-empty pali substrings
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        def expand_from_center(i, j):
            while s[i] == s[j]:
                dp[i][j] = True
                if i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                else:
                    break

        for i in range(n):
            expand_from_center(i, i)
            if i + 1 < n:
                expand_from_center(i, i + 1)

        for i in range(n - 2):
            if dp[0][i]:
                for j in range(i + 1, n - 1):
                    if dp[i + 1][j] and dp[j + 1][n - 1]:
                        return True

        return False
