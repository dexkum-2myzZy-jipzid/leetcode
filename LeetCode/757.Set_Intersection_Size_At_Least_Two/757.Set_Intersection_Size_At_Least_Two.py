#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        # main idea find more element in overlap
        # [1,3],[1,4] 2,3

        # sort by end
        # [[1,3],[1,4],[2,5],[3,5]]
        # first [2,3, 5]
        # if [2, 3] in next interval:
        #     continue
        # elif overlap one elment: # [3,5]
        #     add current end time in
        # else no overlap:
        #     add end, end -1

        intervals.sort(key=lambda x: (x[1], -x[0]))

        n = len(intervals)

        res = 2
        a, b = intervals[0][1] - 1, intervals[0][1]

        for i in range(1, n):
            s, e = intervals[i]

            if s <= a and b <= e:
                continue
            elif s <= b:
                res += 1
                a, b = b, e
            else:  # b < s
                res += 2
                a, b = e - 1, e

        return res
