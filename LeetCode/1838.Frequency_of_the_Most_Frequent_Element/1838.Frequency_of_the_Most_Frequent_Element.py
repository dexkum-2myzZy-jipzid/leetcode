#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # sort nums
        # sliding window
        # num[right] * (right - left + 1) - sum(nums[left:right]) <= k
        #     res = right - left + 1

        nums.sort()

        left = 0
        # the max length
        res = 0
        # sum(nums[left:right])
        total = 0
        for right, num in enumerate(nums):
            total += num

            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1)

        return res
