#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 2**31 - 1
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 2

        while right * right < num:
            right *= 2
            left *= 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
