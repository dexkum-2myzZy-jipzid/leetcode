#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def centeredSubarrays(self, nums: list[int]) -> int:
        n = len(nums)

        res = 0
        for i, num in enumerate(nums):
            total = 0
            elements = set()
            for j in range(i, n):
                total += nums[j]
                elements.add(nums[j])
                if total in elements:
                    res += 1

        return res
