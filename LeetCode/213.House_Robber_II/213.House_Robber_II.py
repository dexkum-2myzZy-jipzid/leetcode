#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def rob(self, nums: list[int]) -> int:

        # dp[i]: two options
        # 1. skip: dp[i-1]
        # 2. take: dp[i-2] + nums[i]

        # edge case:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        # 0 -> n-2
        dp = [0] * n
        # init dp
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        if n == 2:
            return dp[1]

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # 1 -> n-1
        dp2 = [0] * n
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        return max(dp[n - 2], dp2[n - 1])


class Solution2:
    def rob(self, nums: list[int]) -> int:

        # dp[i]: two options
        # 1. skip: dp[i-1]
        # 2. take: dp[i-2] + nums[i]

        # edge case:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        def helper(houses: list[int]) -> int:
            prev1, prev2 = houses[0], max(houses[0], houses[1])
            for i in range(2, len(houses)):
                curr = max(prev2, prev1 + houses[i])
                prev1, prev2 = prev2, curr
            return prev2

        first = helper(nums[:-1])
        second = helper(nums[1:])

        return max(first, second)
