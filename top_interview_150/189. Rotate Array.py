#!/usr/bin/env python3

# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:n-k] = nums[:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        nums[:] = nums[::-1]
