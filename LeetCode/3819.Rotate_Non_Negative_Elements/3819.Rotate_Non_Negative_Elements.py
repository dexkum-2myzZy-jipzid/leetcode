#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def rotateElements(self, nums: list[int], k: int) -> list[int]:
        non_neg = [num for num in nums if num >= 0]

        if len(non_neg) == 0:
            return nums

        k %= len(non_neg)

        res = []
        i = 0
        for num in nums:
            if num < 0:
                res.append(num)
            else:
                idx = (i + k) % len(non_neg)
                res.append(non_neg[idx])
                i += 1

        return res
