#!/usr/bin/env python3

import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 2

        # backtrack, input: ith operation, mask(which nums are taken)

        @cache
        def dfs(idx, mask):
            # all nums are taken
            if mask == (1 << m) - 1 or idx > n:
                return 0

            res = 0
            for i, x in enumerate(nums):
                # ith num are already been taken
                if mask & (1 << i):
                    continue
                for j in range(i + 1, m):
                    y = nums[j]
                    if not mask & (1 << j):
                        # take jth nums
                        new_mask = mask | (1 << i) | (1 << j)
                        res = max(res, dfs(idx + 1, new_mask) + idx * (math.gcd(x, y)))
            return res

        return dfs(1, 0)
