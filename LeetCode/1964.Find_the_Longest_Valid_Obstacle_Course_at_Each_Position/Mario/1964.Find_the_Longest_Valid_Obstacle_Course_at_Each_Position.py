#!/usr/bin/env python3


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # find longest obstacle course
        # 1. choose num
        # 2. include ith obstacle
        # 3. keep same order, subsequence
        # 4. obstacles[i] >= obstacles[i-1]

        # [3,1,5,6,4,2]
        #  3 / 1 / 1, 5 / 1, 5, 6 /1, 4/ 1,2
        # 1 / 1/ 2/ 3 / 2/ 2

        # (get LIS, but it should end with obstacles[i] ) * n

        n = len(obstacles)

        tails = []
        res = []

        for i, o in enumerate(obstacles):
            idx = bisect.bisect_right(tails, o)
            if idx == len(tails):
                tails.append(o)
            else:
                tails[idx] = o
            res.append(idx + 1)

        return res
