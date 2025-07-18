#!/usr/bin/env python3


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # 1. from left to right
        # 2. target[i] = words[j][k]
        # 3. used kth, can't use xth <= k in every word

        # dp[len(word)][a - z]:
        # "aba" i = 1, b
        # [1-2] to find b,
        # 1th b: [0,0] a
        # 2th b: 1th b + [1, 1] a

        MOD = 10**9 + 7
        m, n = len(words), len(words[0])
        count = [[0] * 26 for _ in range(n)]

        for w in words:
            for i, c in enumerate(w):
                j = ord(c) - ord("a")
                count[i][j] += 1

        # dp
        dp = [[0] * 26 for _ in range(n)]
        # init dp

        for i, c in enumerate(target):
            left_letter_count = len(target) - (i + 1)
            idx = ord(c) - ord("a")
            res = 0
            for j in range(n - left_letter_count - 1, i - 1, -1):
                if count[j][idx] > 0:
                    if i == 0:
                        dp[j][idx] = count[j][idx]
                    else:
                        # find previous letter, accumulate count
                        prev = ord(target[i - 1]) - ord("a")
                        prev_count = 0
                        for k in range(i - 1, j):
                            if dp[k][prev] > 0:
                                prev_count = (prev_count + dp[k][prev]) % MOD
                        dp[j][idx] = (count[j][idx] * prev_count) % MOD
                        res = (res + dp[j][idx]) % MOD

        # for r in dp:
        #     print(r)

        return res


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # dp[i][j] means the num of way word[:i] form target[:j]
        # dp[i][j] state transition equation
        # 1. not pick current col, dp[i][j] = dp[i][j-1]
        # 2. pick current col: dp[i][j] += dp[i-1][j-j] * count[target[j]]

        MOD = 10**9 + 7
        target = "#" + target

        m, n = len(words[0]), len(target)

        # counter
        count = [Counter() for _ in range(m)]
        for w in words:
            for i, c in enumerate(w):
                count[i][c] += 1

        # dp
        dp = [[0] * (m + 1) for _ in range(n)]
        # init dp: every col in word can form empty str
        for i in range(m + 1):
            dp[0][i] = 1

        for i in range(1, n):
            cur = target[i]
            left = n - i
            for j in range(1, m + 1):
                # not take current col
                dp[i][j] = dp[i][j - 1]
                # take current col
                if cur in count[j - 1]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * count[j - 1][cur]) % MOD

        # for r in dp:
        #     print(r)

        return dp[n - 1][m]
