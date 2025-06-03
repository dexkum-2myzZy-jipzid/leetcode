#!/usr/bin/env python3


# dfs
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # i:s1, j:s2, k:s3
        @cache
        def dfs(i, j, k):
            if i == m and j == n and k == len(s3):
                return True

            res = False
            if 0 <= i < m and s1[i] == s3[k]:
                res |= dfs(i + 1, j, k + 1)

            if 0 <= j < n and s2[j] == s3[k]:
                res |= dfs(i, j + 1, k + 1)

            return res

        return dfs(0, 0, 0)


# 2 dimensional dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # dp[i][j] i means s1 index, j means s2 index, i+j means s3 index
        # dp[i][j] = (dp[i-1][j] and s1[i] == s3[i+j] ) or (dp[i][j-1] and s2[j] == s3[i+j])

        # init dp
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # s1 is "", compare s2 with s3
        for i in range(1, n + 1):
            if dp[0][i - 1] and s2[i - 1] == s3[i - 1]:
                dp[0][i] = True
            else:
                break

        # s2 is "", compare s1 with s3
        for i in range(1, m + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return dp[m][n]


# optimize to 1 dimensional dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:  # s1 = s2 = s3 = ""
                    dp[0] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = (dp[j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[j] and s1[i - 1] == s3[i + j - 1]
                    )

        return dp[n]
