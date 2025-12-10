#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:

        # binary search to find max total sweetness i can get
        # function can_cut(mid),
        # if can, left = mid + 1,
        # if not, right = mid

        def can_cut(mid: int) -> bool:
            # should be k + 1
            chunk = 0
            cur = 0
            for s in sweetness:
                cur += s
                if cur >= mid:
                    cur = 0
                    chunk += 1

            return chunk >= k + 1

        left, right = min(sweetness), sum(sweetness) // (k + 1)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if can_cut(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
