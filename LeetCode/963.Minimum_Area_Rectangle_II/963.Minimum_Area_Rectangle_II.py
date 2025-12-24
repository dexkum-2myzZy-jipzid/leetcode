#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from math import inf, sqrt


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        n = len(points)
        if n < 4:
            return 0

        groups = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
                groups[(dis, mx, my)].append((points[i], points[j]))

        res = inf

        for k, v in groups.items():
            if len(v) < 2:
                continue
            m = len(v)
            for i in range(m):
                p1, p2 = v[i]
                for j in range(i + 1, m):
                    p3, p4 = v[j]

                    # p1 to p3
                    side13 = sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
                    # p1 to p4
                    side14 = sqrt((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2)

                    res = min(res, side13 * side14)

        return res if res != inf else 0
