#!/usr/bin/env python3


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        vals = [key for key in sorted(count)]

        n = len(vals)
        dp = [v * count[v] for v in vals]

        for i in range(1, n):
            if vals[i - 1] == vals[i] - 1:
                # can't add vals[i-1] points
                if i >= 2:
                    dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
                else:
                    dp[i] = max(dp[i - 1], dp[i])
            else:
                dp[i] += dp[i - 1]

        # print(f"vals: {vals}\ndp: {dp}")

        if n == 1:
            return dp[0]
        else:
            return max(dp[-1], dp[-2])
