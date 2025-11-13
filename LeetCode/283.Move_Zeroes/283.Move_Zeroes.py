#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0  # next non zero position / first zero index in current nums

        for i in range(len(nums)):
            if nums[i] != 0:
                if non_zero < i:
                    nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
