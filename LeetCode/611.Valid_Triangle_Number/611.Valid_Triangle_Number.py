#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        n = len(nums)
        nums.sort()

        res = 0
        for k in range(n - 1, -1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # a in [nums[i]...nums[j-1]]
                    res += j - i
                    j -= 1
                else:
                    i += 1

        return res
