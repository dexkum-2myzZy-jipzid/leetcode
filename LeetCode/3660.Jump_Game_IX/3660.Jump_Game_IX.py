#!/usr/bin/env python3

from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_max = [0] * n
        suffix_min = [0] * n

        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        cuts = []
        for i in range(0, n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                cuts.append(i + 1)

        # print(prefix_max)
        # print(suffix_min)
        # print(cuts)

        cuts.append(n)

        res = [0] * n
        i = 0
        for cut in cuts:
            seg_val = prefix_max[cut - 1]
            while i < cut:
                res[i] = seg_val
                i += 1

        return res
