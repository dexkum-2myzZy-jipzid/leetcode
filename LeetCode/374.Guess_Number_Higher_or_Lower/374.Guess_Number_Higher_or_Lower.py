#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:  # num == pick
                return mid
            elif guess(mid) == -1:  # num > pick
                right = mid - 1
            else:  # num < pick
                left = mid + 1
        return -1


class Solution2:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            if guess(mid) == 1:  # num < pick
                left = mid + 1
            else:
                right = mid

        return left
