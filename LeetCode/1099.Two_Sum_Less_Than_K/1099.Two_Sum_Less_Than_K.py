#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()

        res = -1
        i, j = 0, len(nums) - 1

        while i < j:
            curr = nums[i] + nums[j]
            if curr < k:
                res = max(curr, res)
                i += 1
            else:
                j -= 1

        return res
