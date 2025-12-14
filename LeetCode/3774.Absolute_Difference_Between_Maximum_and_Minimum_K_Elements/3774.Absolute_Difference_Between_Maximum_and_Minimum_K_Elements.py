#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def absDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[:k]) - sum(nums[-k:]))
