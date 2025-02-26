#!/usr/bin/env python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)

        # init dp
        dp[1] = nums[0]

        for i in range(2, n + 1):
            # rob current house
            cur = dp[i - 2] + nums[i - 1]
            # not rob current house
            pre = dp[i - 1]

            dp[i] = max(cur, pre)

        return dp[n]


"""
n = len(nums)
dp[n+1]
dp[i] robber can rob max amount of money from [1-i]
[1, 2, 3, 1]
[0, 1, 2, 4, 4]
"""