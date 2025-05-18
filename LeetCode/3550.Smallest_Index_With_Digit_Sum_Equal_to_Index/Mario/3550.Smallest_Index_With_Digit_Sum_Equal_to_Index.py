#!/usr/bin/env python3


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i, num in enumerate(nums):
            res = sum(map(int, str(num)))

            if res == i:
                return i

        return -1
