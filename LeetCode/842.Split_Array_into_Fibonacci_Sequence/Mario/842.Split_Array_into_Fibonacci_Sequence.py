#!/usr/bin/env python3

from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # cut num into several segments
        # dp[i][j] represents can be fibonacci-like or not, for segment [i, j]
        n = len(num)
        res = []

        def dfs(i, path):
            nonlocal res
            if i == n:
                if len(path) >= 3:
                    res = path
                    return True
                return False

            for j in range(i + 1, n + 1):
                cur = int(num[i:j])
                # f < 2 ** 31
                if cur > 2**31:
                    break
                # no leading zero
                if num[i] == "0" and j > i + 1:
                    break
                # f1 + f2 = f3
                if len(path) >= 2 and path[-2] + path[-1] != cur:
                    continue
                path.append(cur)
                if dfs(j, path):
                    return True
                path.pop()

            return False

        dfs(0, [])
        return res
