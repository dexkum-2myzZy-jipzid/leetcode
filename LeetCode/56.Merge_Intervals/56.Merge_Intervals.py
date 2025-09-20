#!/usr/bin/env python3


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # intervals[i][1] >= intervals[i+1][0], then merge

        intervals.sort(key=lambda x: x[0])
        res = []
        for e in intervals:
            if res and e[0] <= res[-1][1]:
                last = res[-1]
                res[-1] = [last[0], max(last[1], e[1])]
            else:
                res.append(e)

        return res
