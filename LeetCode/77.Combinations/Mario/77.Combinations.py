#!/usr/bin/env python3


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtracking(i, path):
            if i == k:
                res.append(path[:])
                return

            # select num from i+1 to n 1 -> 4 / 2 -> 4
            for j in range(i + 1, n + 1):
                path.append(j)
                # print(path)
                backtracking(j + 1, path)
                path.pop()

        backtracking(0, [])

        return res
