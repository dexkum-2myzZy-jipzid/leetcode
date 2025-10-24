#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first, second, third = None, None, None

        for num in nums:
            if first == num or second == num or third == num:
                continue

            if first is None or num > first:
                third, second, first = second, first, num
            elif second is None or num > second:
                third, second = second, num
            elif third is None or num > third:
                third = num
            # print(first, second, third)

        return third if third is not None else first
