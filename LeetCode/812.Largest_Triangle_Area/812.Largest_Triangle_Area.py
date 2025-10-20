#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        # y = kx + b
        # if i have 2 points, i can get k and b
        # y1 = kx1 + b
        # h = abs(diff b)

        n = len(points)

        res = 0.0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                ab = (x2 - x1, y2 - y1)
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    ac = (x3 - x1, y3 - y1)
                    area = 0.5 * abs(ab[0] * ac[1] - ab[1] * ac[0])
                    res = max(res, area)

        return res
