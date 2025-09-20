#!/usr/bin/env python3


# dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # possible combination
        # knapsack problem, dp

        dp = [0] * (target + 1)
        # init dp
        dp[0] = 1

        # nums.sort()

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]
