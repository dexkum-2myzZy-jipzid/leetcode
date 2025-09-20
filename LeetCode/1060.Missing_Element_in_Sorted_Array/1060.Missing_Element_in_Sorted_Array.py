#!/usr/bin/env python3


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # count how many missing elements before nums[i]
        def missing(i):
            # nums[i] - nums[0] + 1 - (i+1)
            return nums[i] - nums[0] - i

        # how many missing elements in nums
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        # so result in the [nums[0], nums[-1]] range
        left, right = 0, n - 1
        while left < right:  # left = right = n-1
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid

        # cur left make nums[left-1] < k <= nums[left]
        return nums[left - 1] + k - missing(left - 1)

        # kth smallest / largest -> (heap / binary search)
