#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        # binary search to find smallest divisor

        def get_sum(k: int) -> int:
            res = 0
            for num in nums:
                res += (num + k - 1) // k
            return res

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if get_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
            # print(f"left:{left}\tright:{right}")

        return left
