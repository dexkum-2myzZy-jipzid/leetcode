#!/usr/bin/env python3


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i, p in enumerate(points):
            counter = defaultdict(int)
            xi, yi = p
            overlap = 0
            max_points = 0

            for j in range(n):
                xj, yj = points[j]
                if i == j:
                    continue
                if xi == xj and yi == yj:
                    overlap += 1
                    continue
                dx, dy = xi - xj, yi - yj  # 4, 6

                g = gcd(dx, dy)  # 2
                slope = (dy // g, dx // g)  # 2,3
                counter[slope] += 1
                max_points = max(max_points, counter[slope])

            res = max(res, max_points + 1 + overlap)

        return res
