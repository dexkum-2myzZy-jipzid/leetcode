#!/usr/bin/env python3
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        # k positive int
        # max diff is minimized
        # n >= 4 & k >= 2

        # get int which product to be n
        arr = []
        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)

        m = len(arr)

        # print(arr)
        res = []
        max_diff = inf

        def dfs(i, remain, k, path):
            nonlocal res, max_diff
            if k == 0:
                if remain == 1:
                    diff = path[-1] - path[0]
                    if diff < max_diff:
                        max_diff = diff
                        res = path[:]
                return

            for j in range(i, m):
                if remain % arr[j] != 0:
                    continue
                dfs(j, remain // arr[j], k - 1, path + [arr[j]])

        dfs(0, n, k, [])

        return res
