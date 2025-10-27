#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        # means find subarray, in this subarray only two nums,
        # return max length of this subarray

        # edge case:
        # fruits is empty, return 0
        if not fruits:
            return 0

        # sliding window
        # dic keep track of window, len(dic) <= 2
        window = defaultdict(int)
        res = l = 0

        for r, f in enumerate(fruits):
            # shift right, dic[nums[right]] += 1
            window[f] += 1

            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
