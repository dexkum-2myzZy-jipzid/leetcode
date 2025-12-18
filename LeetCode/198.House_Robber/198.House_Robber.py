#!/usr/bin/env python3


class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp[i] represent max money i can rob in nums[:i]
        # dp[i] two choice
        # dp[i] = max(dp[i-1], dp[i-2] + num)

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        f1, f2 = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            current = max(f1 + nums[i], f2)
            f1, f2 = f2, current

        return f2
