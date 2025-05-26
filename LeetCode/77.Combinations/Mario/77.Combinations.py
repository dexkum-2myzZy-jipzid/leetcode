#!/usr/bin/env python3


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        path = []

        def backtrack(start):
            # print(path)
            if len(path) == k:
                res.append(path[:])
                return

            # The loop upper bound 'n - (k - len(path)) + 2' is a pruning optimization.
            # It ensures there are enough remaining numbers to complete a valid combination,
            # thus reducing unnecessary recursive calls.
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)

        return res
