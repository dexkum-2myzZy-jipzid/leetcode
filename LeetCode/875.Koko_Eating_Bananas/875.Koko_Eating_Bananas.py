#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def check(k: int) -> bool:
            res = 0
            for p in piles:
                res += (p + k - 1) // k
                if res > h:
                    return False
            return res <= h

        left, right = 1, max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
