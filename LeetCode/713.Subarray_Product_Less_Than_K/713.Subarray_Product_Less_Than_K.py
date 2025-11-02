#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        left = 0
        wind_prod = 1
        res = 0

        for right, num in enumerate(nums):

            if num >= k:
                left = right + 1
                wind_prod = 1
                continue

            while left < right and wind_prod * num >= k:
                wind_prod //= nums[left]
                left += 1

            wind_prod *= num

            res += right - left + 1

        return res
