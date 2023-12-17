#!/usr/bin/env python3

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(2, len(nums), 3):
            if nums[i] - nums[i-2] > k:
                return []
            res.append(nums[i-2:i+1])
        return res
