#!/usr/bin/env python3


# dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # define dp[i] include current ith num max sum val

        # init dp
        dp = [0] * n
        dp[0] = nums[0]

        res = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])

        return res


# Kadane's algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = -math.inf, 0
        for i, num in enumerate(nums):
            cur += num
            res = max(cur, res)
            if cur < 0:
                cur = 0

        return res
