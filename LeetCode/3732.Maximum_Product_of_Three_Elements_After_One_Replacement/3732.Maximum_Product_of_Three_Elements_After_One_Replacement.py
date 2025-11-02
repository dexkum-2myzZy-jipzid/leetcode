#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        #  must replace exactly one element

        MAX = 10**5
        MIN = -(10**5)

        nums.sort(key=lambda x: abs(x))
        arr = nums[-2:]

        prod = arr[0] * arr[1]

        return max(prod * MAX, prod * MIN)
