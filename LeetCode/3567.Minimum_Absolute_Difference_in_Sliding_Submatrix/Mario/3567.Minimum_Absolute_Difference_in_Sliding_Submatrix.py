#!/usr/bin/env python3


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        res = []
        for i in range(m - k + 1):
            sub = []
            for j in range(n - k + 1):
                # i, j is start point of submatirx
                s = set()
                for u in range(i, i + k):
                    for v in range(j, j + k):
                        s.add(grid[u][v])
                if len(s) == 1:
                    sub.append(0)
                else:
                    arr = list(s)
                    arr.sort()
                    # print(arr)
                    diff = math.inf
                    for a in range(len(arr) - 1):
                        diff = min(diff, arr[a + 1] - arr[a])
                    sub.append(diff)
            res.append(sub)

        return res
