#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf


class Solution:
    def binarySearchableNumbers(self, nums: list[int]) -> int:
        # if nums[i] is searchable
        # all elements on the left side, index < i, should nums[index] < nums[i]
        # all elements on the right side, index > i, should nums[index] > nums[i]
        # nums[i]

        n = len(nums)

        prefix_max = [0] * n
        curr_max = -inf
        for i, num in enumerate(nums):
            prefix_max[i] = curr_max
            curr_max = max(curr_max, nums[i])

        suffix_min = [0] * n
        curr_min = inf
        for i in range(n - 1, -1, -1):
            suffix_min[i] = curr_min
            curr_min = min(curr_min, nums[i])

        result = 0
        for i, num in enumerate(nums):
            if prefix_max[i] < num < suffix_min[i]:
                result += 1

        return result
