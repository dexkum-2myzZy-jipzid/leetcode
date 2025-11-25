#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, 2

        while right * right < x:
            right *= 2
            left *= 2

        ans = left

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans
