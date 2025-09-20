#!/usr/bin/env python3


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # iterate interval in intervals,
        res = []
        inserted = False
        for cur in intervals:

            # cur is the left side of new interval
            if cur[1] < newInterval[0]:
                res.append(cur)
            # right side
            elif cur[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(cur)
            else:
                newInterval[0] = min(cur[0], newInterval[0])
                newInterval[1] = max(cur[1], newInterval[1])

        if not inserted:
            res.append(newInterval)

        return res
