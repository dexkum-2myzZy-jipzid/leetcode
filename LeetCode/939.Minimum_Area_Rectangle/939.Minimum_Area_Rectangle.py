#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from math import inf


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:

        # sort points:
        # [[1,1],[1,3],[2,2],[3,1],[3,3]]

        # columns: {x:[(),()]} => {1:[(1,1), (1,3)], 3:[(3,1), (3,3)], 2:[(2,2)]}

        # [1, 2, 3]

        points.sort(key=lambda x: (x[0], x[1]))

        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        # ({y1, y2) : x}
        last_x = {}

        res = inf
        for x in sorted(columns.keys()):
            array = columns[x]

            n = len(array)
            for i in range(n):
                y1 = array[i]
                for j in range(i + 1, n):
                    y2 = array[j]

                    if (y1, y2) in last_x:
                        area = abs(last_x[(y1, y2)] - x) * (y2 - y1)
                        res = min(res, area)

                    last_x[(y1, y2)] = x

        return res if res != inf else 0
