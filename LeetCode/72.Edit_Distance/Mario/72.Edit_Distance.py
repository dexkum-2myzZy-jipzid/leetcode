#!/usr/bin/env python3


# multi dimensional dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] the min num of operations word1[:i] convert to word2[:j]
        # insert: dp[i][j-1] + 1
        # delete: dp[i-1][j] + 1
        # replace: dp[i-1][j-1] + 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # word1 = "xxx"  word2 = ""
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1

        # word1 = "" word2 = "xxx"
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        # insert
                        dp[i][j - 1] + 1,
                        # delete
                        dp[i - 1][j] + 1,
                        # replace
                        dp[i - 1][j - 1] + 1,
                    )

        return dp[m][n]


# 1 dimensional dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] the min num of operations word1[:i] convert to word2[:j]
        # insert: dp[i][j-1] + 1
        # delete: dp[i-1][j] + 1
        # replace: dp[i-1][j-1] + 1
        dp = [0] * (n + 1)

        # word1 = "" word2 = "xxx"
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

        # print(dp)

        for i in range(1, m + 1):
            pre = dp[:]
            dp[0] = i  # 把 word1 的前 i 个字符变成空串 word2[:0]，需要的操作数
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre[j - 1]
                else:
                    dp[j] = min(
                        # insert
                        dp[j - 1] + 1,
                        # delete
                        pre[j] + 1,
                        # replace
                        pre[j - 1] + 1,
                    )

        return dp[n]
