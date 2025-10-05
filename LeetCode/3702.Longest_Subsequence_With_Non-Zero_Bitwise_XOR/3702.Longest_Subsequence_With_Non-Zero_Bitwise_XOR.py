#!/usr/bin/env python3

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # 0 ^ 1 = 1
        n = len(nums)
        any_zero = False
        res = 0
        for num in nums:
            res ^= num
            if res != 0:
                any_zero = True

        if res != 0:
            return n
        if any_zero:
            return n-1

        return 0