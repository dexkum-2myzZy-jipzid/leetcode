#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # sort nums
        # nums[i] + nums[i+1] > nums[i+2]

        nums.sort()

        n = len(nums)

        for i in range(n - 1, 1, -1):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if a + b > c:
                return a + b + c

        return 0
