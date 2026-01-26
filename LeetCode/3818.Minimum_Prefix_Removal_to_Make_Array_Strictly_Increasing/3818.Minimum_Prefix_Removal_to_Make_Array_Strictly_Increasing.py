#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minimumPrefixLength(self, nums: list[int]) -> int:

        cnt = 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                cnt += 1
                continue
            else:
                break

        return len(nums) - cnt
