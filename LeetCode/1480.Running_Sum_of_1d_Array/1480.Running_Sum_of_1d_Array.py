#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = 0
        res = []
        for num in nums:
            running_sum += num
            res.append(running_sum)
        return res
