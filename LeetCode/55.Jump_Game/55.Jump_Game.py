#!/usr/bin/env python3


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        n = len(nums)
        max_reach = 0

        for i, step in enumerate(nums):
            if i > max_reach:
                return False

            max_reach = max(i + step, max_reach)
            if max_reach >= n - 1:
                return True

        return False
