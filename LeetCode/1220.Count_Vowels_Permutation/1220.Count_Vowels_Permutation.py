#!/usr/bin/env python3


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 1. every is lower case vowel
        # 2. "a" + "e"
        # 3. "e" + "a" / "i"
        # 4. "i" not + "i"
        # 5. "o" + "i"/"u"
        # 6. "u" + "a"

        MOD = 10**9 + 7

        # 0:a, 1:e 2:i 3:o 4:u
        # dp[i][x] means the num of ith which end with x vowel

        dp = [[0] * 5 for _ in range(n)]
        # init
        dp[0] = [1, 1, 1, 1, 1]

        for i in range(1, n):
            # a
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD
            # e
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            # i
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
            # o
            dp[i][3] = (dp[i - 1][2]) % MOD
            # u
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD

        res = 0
        for val in dp[n - 1]:
            res += val
            res %= MOD

        return res


# st: o(1)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 1. every is lower case vowel
        # 2. "a" + "e"
        # 3. "e" + "a" / "i"
        # 4. "i" not + "i"
        # 5. "o" + "i"/"u"
        # 6. "u" + "a"

        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            aa = (e + i + u) % MOD  # a <- e, i, u
            ee = (a + i) % MOD  # e <- a, i
            ii = (e + o) % MOD  # i <- e, o
            oo = i % MOD  # o <- i
            uu = (i + o) % MOD  # u <- i, o

            a, e, i, o, u = aa, ee, ii, oo, uu

        return (a + e + i + o + u) % MOD
