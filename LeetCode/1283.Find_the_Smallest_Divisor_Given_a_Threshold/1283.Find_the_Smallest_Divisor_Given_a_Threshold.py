#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import ceil


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        # main idea is binary search, left = 1, right = max(nums) + 1

        # mid = (left + right) // 2

        # try iterate all every element in nums, x = sum(ceil(element / mid))

        # if x > threshold, left = mid +1, else x <= threshold, right = mid

        left, right = 1, max(nums) + 1

        def helper(divisor: int) -> bool:
            res = 0
            for num in nums:
                res += ceil(num / divisor)
            return res <= threshold

        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1

        return left
