#!/usr/bin/env python3


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [1, 8], [7, 16] two range
        points.sort(key=lambda x: x[0])

        merged = [points[0]]

        for i in range(1, len(points)):
            cur = points[i]
            last = merged[-1]
            # overlap
            if last[1] >= cur[0]:
                merged[-1] = [cur[1], min(last[1], cur[1])]
            else:
                merged.append(cur)

        return len(merged)
