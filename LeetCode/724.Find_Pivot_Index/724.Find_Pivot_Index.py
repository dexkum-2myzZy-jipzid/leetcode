#!/usr/bin/env python3


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # i = pivot index
        # sum([:i]) == sum(nums[i+1:])
        # leftmost pivot index or -1
        n = len(nums)
        total = sum(nums)
        cur = 0
        for i, num in enumerate(nums):
            if i < n and cur * 2 == (total - nums[i]):
                return i
            cur += num

        return -1
