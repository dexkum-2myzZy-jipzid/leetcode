#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # 1:[0, 2, 3]

        same_val_idx = defaultdict(list)

        for i, num in enumerate(nums):
            same_val_idx[num].append(i)

        best = inf

        for _, arr in same_val_idx.items():
            if len(arr) <= 2:
                continue
            else:
                first, second = arr[0], arr[1]
                for i in range(2, len(arr)):
                    third = arr[i]
                    good = third - first + third - second + second - first
                    best = min(best, good)
                    first, second = second, third

        return best if best != inf else -1
