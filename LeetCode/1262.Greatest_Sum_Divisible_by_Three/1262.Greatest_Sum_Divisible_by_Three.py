#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        # [1, 3, 5, 6, 8]
        total = sum(nums)
        if total % 3 == 0:
            return total

        nums.sort()
        remainder = total % 3
        rem1, rem2 = [], []

        for num in nums:
            if num % 3 == 1:
                rem1.append(num)
            elif num % 3 == 2:
                rem2.append(num)

        if remainder == 1:
            # only 1 element which element %  3 == 1
            first = rem1[0] if rem1 else inf
            # or 2 elements which each element % 3 == 2
            second = sum(rem2[:2]) if len(rem2) >= 2 else inf

            return int(total - min(first, second))

        elif remainder == 2:
            # only 1 element which element %  3 == 2
            first = rem2[0] if rem2 else inf
            # or 2 elements which each element % 3 == 1
            second = sum(rem1[:2]) if len(rem1) >= 2 else inf

            return int(total - min(first, second))

        return 0
