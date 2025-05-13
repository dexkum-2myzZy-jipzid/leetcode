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
