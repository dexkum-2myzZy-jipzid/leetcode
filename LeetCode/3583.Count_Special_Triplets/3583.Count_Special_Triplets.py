#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict, Counter
import bisect


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        # nums = [6,3,6]
        # 1. dic: {6:[0, 2], 3:[1]}

        # 2. iterate nums, j = 1,
        # num = 3, looking for num = 6

        MOD = 10**9 + 7

        n = len(nums)
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)

        result = 0
        for j, num in enumerate(nums):
            double = num * 2
            if double not in idx_map:
                continue
            else:
                array = idx_map[double]
                # how many idx < j
                idx = bisect.bisect_right(array, j)
                if idx == len(array) or idx == 0:
                    continue
                else:
                    i_count = (idx - 1) if num == 0 else idx
                    k_count = len(array) - idx
                    result = (result + i_count * k_count) % MOD

        return result


class Solution2:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if n < 3:
            return 0

        right_count = Counter(nums)
        left_count = Counter()

        result = 0
        for j, num in enumerate(nums):
            double = 2 * num
            right_count[num] -= 1

            i_count = left_count[double]
            k_count = right_count[double]

            result = (result + i_count * k_count) % MOD

            left_count[num] += 1

        return result
