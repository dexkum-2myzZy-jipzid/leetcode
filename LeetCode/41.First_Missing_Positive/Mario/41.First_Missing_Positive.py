#!/usr/bin/env python3


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Find the smallest missing positive integer in-place.
        Two passes:
          1. For each index i, swap nums[i] into its correct slot nums[nums[i]−1] while it’s in [1..n].
          2. Scan for the first index i where nums[i] ≠ i+1; that i+1 is the answer.
        """

        n = len(nums)

        for i in range(n):

            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
