#!/usr/bin/env python3

from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        res = 0
        for h in houses:
            p = bisect_left(heaters, h)
            if p == 0:
                dis = abs(heaters[0] - h)
            elif p == len(heaters):
                dis = abs(heaters[-1] - h)
            else:
                left = h - heaters[p-1]
                right = heaters[p] - h
                dis = min(left, right)
            res = max(res, dis)
        
        return res