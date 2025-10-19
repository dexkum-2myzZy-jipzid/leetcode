#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)
        n = 1
        while n * k <= 200 and n * k in nums_set:
            n += 1
        return n * k
