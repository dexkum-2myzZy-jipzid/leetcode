#!/usr/bin/env python3

# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return i
