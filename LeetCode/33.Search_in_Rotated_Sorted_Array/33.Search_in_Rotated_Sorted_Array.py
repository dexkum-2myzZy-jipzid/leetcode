#!/usr/bin/env python3


# Binary Search
# find pivot, then find target in specific partition
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # find pivot index
        l, r = 0, n - 1
        l = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        # print(f"privot: {l}")

        if target == nums[n - 1]:
            return n - 1
        elif target > nums[n - 1]:
            res = bisect.bisect_left(nums[:l], target)
            if res < l and nums[res] == target:
                return res
            else:
                return -1
        else:
            m = len(nums[l:])
            res = bisect.bisect_left(nums[l:], target)
            if res < m and nums[res + l] == target:
                return res + l
            else:
                return -1


# BinarySearch Direct Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # check left order
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
