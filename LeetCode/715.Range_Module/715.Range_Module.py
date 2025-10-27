#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from math import inf


class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        L, R = left, right
        res = []
        placed = False

        for l, r in self.intervals:
            # current interval total before [L, R)
            if r < L:
                res.append([l, r])
            elif R < l:
                if not placed:
                    res.append([L, R])
                    placed = True
                res.append([l, r])
            else:  # intersect
                L = min(L, l)
                R = max(R, r)

        if not placed:
            res.append([L, R])

        self.intervals = res

    def queryRange(self, left: int, right: int) -> bool:
        # bisect_left: >= left / bisect_right: > left
        idx = bisect.bisect_right(self.intervals, [left, inf]) - 1
        if idx < 0:
            return False
        l, r = self.intervals[idx]
        return l <= left and right <= r

    def removeRange(self, left: int, right: int) -> None:
        res = []
        for l, r in self.intervals:
            if r <= left or l >= right:
                res.append([l, r])
            else:
                if l < left:
                    res.append([l, left])
                if right < r:
                    res.append([right, r])
        self.intervals = res


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
