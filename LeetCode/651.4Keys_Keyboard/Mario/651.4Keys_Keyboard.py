#!/usr/bin/env python3


class Solution:
    def maxA(self, n: int) -> int:
        # 1. A: add 1
        # 2. ctrl+acv: double all previous A
        # 3. ctrl+v : append + A in buffer, must after 2

        # 1. 1 press; 2. 3 press; 3. 1 press

        # dp[i] = dp[i-1] + 1 <= dp[i-3] * 2, store buff, then
        #    dp[i-1] + buff

        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            # press A
            dp[i] = dp[i - 1] + 1
            for j in range(2, i - 1):
                # press ctrl + a,c press ctrl + v  x times
                # x = (i - j + 1 - 2) times
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        # print(dp)

        return dp[n - 1]
