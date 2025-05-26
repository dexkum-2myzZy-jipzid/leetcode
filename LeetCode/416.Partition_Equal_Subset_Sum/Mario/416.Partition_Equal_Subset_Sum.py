#!/usr/bin/env python3


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0-1 knapsack
        # handle edge case
        total = sum(nums)
        if total % 2 == 1 or len(nums) <= 1:
            return False

        half = total // 2  # 11

        # 1 represent yes, 0 represent no
        # dp[i] can be sum i or not
        dp = [False for _ in range(half + 1)]
        dp[0] = True

        for num in nums:
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[half]
