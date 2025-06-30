#!/usr/bin/env python3


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # binary search

        n = len(nums)
        nums.sort()

        def count_valid_parts(k):
            i, count = 0, 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= k:
                    count += 1
                    i += 1
                i += 1
            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count_valid_parts(mid) < p:
                left = mid + 1
            else:
                right = mid

        return left
