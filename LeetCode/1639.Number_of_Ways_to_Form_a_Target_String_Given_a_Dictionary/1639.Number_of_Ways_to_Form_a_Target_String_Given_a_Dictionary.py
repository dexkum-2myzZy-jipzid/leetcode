#!/usr/bin/env python3


# dp
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # left -> right
        # if take xth character,  no more x<=k in nay strings

        # dp[i][j] represents the num of ways to form target[:i] using first j columns of words
        # array[j] = {char: count} for column j
        # if target[i-1] in array[j]:
        #   take jth column: dp[i][j] += dp[i-1][j-1] * count
        #   skip jth column: dp[i][j] += dp[i][j-1]

        MOD = 10**9 + 7

        m, n = len(target), len(words[0])
        arr = [Counter() for _ in range(n)]
        for w in words:
            for i, c in enumerate(w):
                arr[i][c] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 0 character in word form ""
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            t = target[i - 1]
            for j in range(1, n + 1):
                counter = arr[j - 1]

                # skip jth character
                dp[i][j] = dp[i][j - 1]

                # take jth character
                if t in counter:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * counter[t]) % MOD

        # for r in dp:
        #     print(r)

        return dp[m][n]


# dfs
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])

        arr = [Counter() for _ in range(n)]
        for w in words:
            for i, c in enumerate(w):
                arr[i][c] += 1

        # i: index of target, j: index of column in word
        @cache
        def dfs(i, j):
            # Base case: matched all characters in target
            if i == m:
                return 1
            # Base case: ran out of columns but still have characters left in target
            if j == n:
                return 0

            t = target[i]

            # skip j column
            res = dfs(i, j + 1)

            # take j column
            if t in arr[j]:
                res = (res + dfs(i + 1, j + 1) * arr[j][t]) % MOD

            return res

        return dfs(0, 0)
