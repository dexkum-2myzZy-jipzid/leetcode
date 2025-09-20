#!/usr/bin/env python3


class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        # (s[i-1] + s[i]) <= 26
        # dp[i] = dp[i-1] + dp[i-2]

        # startwith '0' return 0

        if s.startswith("0"):
            return 0

        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            cur = s[i - 1]
            if cur != "0":
                dp[i] += dp[i - 1]

            num = int(s[i - 2 : i])
            if 10 <= num <= 26:
                dp[i] += dp[i - 2]

            # can't decode
            if dp[0] == 0:
                return 0

        return dp[n]
