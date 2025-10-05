#!/usr/bin/env python3

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                res += num
            else:
                res -= num
        return res