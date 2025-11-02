#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        nums.sort()

        nums_set = set(nums)
        res = []

        for num in range(nums[0], nums[-1] + 1):
            if num not in nums_set:
                res.append(num)

        return res
