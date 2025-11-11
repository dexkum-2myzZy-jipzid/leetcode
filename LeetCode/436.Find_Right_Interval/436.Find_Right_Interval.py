#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:

        # start_j >= end_i
        # starts_array = []

        starts = [(x[0], i) for i, x in enumerate(intervals)]

        starts.sort(key=lambda x: x[0])

        res = []
        for s, e in intervals:
            idx = bisect.bisect_left(starts, (e, -1))
            if idx == len(starts):
                res.append(-1)
            else:
                res.append(starts[idx][1])

        return res
