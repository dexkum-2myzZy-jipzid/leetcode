#!/usr/bin/env python3


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three way quick sort
        # three pointer (0, 2, current)

        n = len(nums)
        # j: 0, k: 2
        i, j, k = 0, 0, n - 1
        while i <= k:
            cur = nums[i]
            if cur == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif cur == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1
