#!/usr/bin/env python3

from math import inf
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        dp = [inf] * k
        dp[0] = 0
        f = s = 0

        for i, num in enumerate(nums):
            s = (s + num) % k

            # no delete, f + num
            # delete num,
            f = min(f + num, dp[s])

            dp[s] = f

        return f
