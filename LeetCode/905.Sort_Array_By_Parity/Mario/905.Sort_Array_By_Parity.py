#!/usr/bin/env python3


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # two pointer
        # one point to even, one point to every element
        n = len(nums)
        # j point to even
        j = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
