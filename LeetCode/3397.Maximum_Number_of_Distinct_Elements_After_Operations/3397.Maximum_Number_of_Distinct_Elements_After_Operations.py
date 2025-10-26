#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:

        nums.sort()

        last = nums[0] - k
        res = 1

        for i in range(1, len(nums)):

            if last < nums[i] + k:
                last = max(last + 1, nums[i] - k)
                res += 1

        return res
