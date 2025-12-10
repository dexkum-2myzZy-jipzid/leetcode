#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        # binary search to find mini largest sum of split
        # using function can_split_into_k to check mid

        def can_split_into_k(m: int) -> bool:
            group = 1
            cur_sum = 0
            for num in nums:
                cur_sum += num
                if cur_sum > m:
                    cur_sum = num
                    group += 1
                if group > k:
                    return False

            return group <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split_into_k(mid):
                right = mid
            else:
                left = mid + 1

        return left
