#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0
        for key, v in count.items():
            if v % k == 0:
                res += key * v
        return res