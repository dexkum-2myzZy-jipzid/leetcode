#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def arrangeCoins(self, n: int) -> int:

        def get_count(x: int) -> int:
            return (1 + x) * x // 2

        left, right = 1, 2

        while get_count(right) < n:
            right *= 2
            left *= 2

        res = left
        while left <= right:
            mid = left + (right - left) // 2
            count = get_count(mid)
            if count == n:
                return mid
            elif count < n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
