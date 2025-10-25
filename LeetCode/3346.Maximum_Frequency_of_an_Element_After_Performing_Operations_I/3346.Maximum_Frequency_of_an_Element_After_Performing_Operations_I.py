#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)

        diff = defaultdict(int)
        for num in nums:
            diff[num - k] += 1
            diff[num + k + 1] -= 1

        points = sorted(set(diff.keys()) | set(freq.keys()))

        res = cover = 0

        for p in points:
            cover += diff[p]

            cnt = freq[p] if p in freq else 0
            curr = min(numOperations + cnt, cover)
            res = max(res, curr)

        return res
