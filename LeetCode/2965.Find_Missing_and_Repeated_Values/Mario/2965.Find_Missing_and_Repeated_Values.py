#!/usr/bin/env python3

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = []
        for i in range(n**2):
            nums.append(i+1)

        res = []
        for row in grid:
            for num in row:
                if num in nums:
                    nums.remove(num)
                else:
                    res.append(num)
        res.append(nums[0])
        return res
