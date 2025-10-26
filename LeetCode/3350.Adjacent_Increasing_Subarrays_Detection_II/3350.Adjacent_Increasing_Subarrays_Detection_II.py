#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf


class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:

        # previous length / current length

        # nums = [2,5,7,8,9,2,3,4,3,1]

        # 2 ways to update k,
        # 1. k * 2 = (current length) // 2
        # 2. k = min(previous length, current length)
        nums += [-inf]
        prev, curr = 0, 1
        k = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                k = max(k, curr // 2)
                k = max(k, min(prev, curr))
                prev = curr
                curr = 1

        return k
