#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def sortByReflection(self, nums: list[int]) -> list[int]:

        def reverse(num: int) -> int:
            res = 0
            while num > 0:
                res = (res << 1) | (num & 1)
                num >>= 1
            return res

        return sorted(nums, key=lambda x: (reverse(x), x))
