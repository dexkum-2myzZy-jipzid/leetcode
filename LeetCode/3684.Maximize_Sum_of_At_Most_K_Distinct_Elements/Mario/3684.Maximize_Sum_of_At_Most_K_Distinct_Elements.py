#!/usr/bin/env python3


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(key=lambda x: -x)
        n = len(nums)
        return nums[: min(n, k)]
