#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maximizeExpressionOfThree(self, nums: list[int]) -> int:
        # max(a + b - c)
        nums.sort()
        return sum(nums[-2:]) - nums[0]
