#!/usr/bin/env python3


class Solution:
    def numDecodings(self, s: str) -> int:
        # A -> 1 ... Z -> 26
        # "*" -> [1 , 9]
        # "11" -> "26" has 2 ways to decode

        # dp[i]: for s[:i] the number of ways to decode it
        # dp[i] = s[i] * dp[n-1] + s[i-1:i] * dp[n-2]
        # s[i] == "*" way = 9
        # 0 < int(s[i]) < 10: 1

        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)

        # init dp
        dp[0] = 1
        if s[0] == "*":
            dp[1] = 9
        elif s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, n + 1):
            # 1 digit case
            cur = s[i - 1]
            if cur == "*":
                dp[i] = (dp[i] + 9 * dp[i - 1]) % MOD
            elif 0 < int(cur) < 10:
                dp[i] = (dp[i] + dp[i - 1]) % MOD

            # 2 digits case
            pre = s[i - 2]
            way = 0
            #
            if pre == "1":
                if cur == "0":  # 10
                    way = 1
                elif cur == "*":  # 11 - 19
                    way = 9
                else:  # 16
                    way = 1
            elif pre == "2":
                if cur == "0":  # 20
                    way = 1
                elif cur == "*":  # 21 - 26
                    way = 6
                elif int(cur) < 7:  # 26
                    way = 1
            elif pre == "*":
                if cur == "0":  # 20
                    way = 2
                elif cur == "*":  # 11 - 19, 21-26
                    way = 15
                elif int(cur) <= 6:  # 16, 26
                    way = 2
                else:
                    way = 1

            dp[i] = (dp[i] + way * dp[i - 2]) % MOD

        return dp[n]
