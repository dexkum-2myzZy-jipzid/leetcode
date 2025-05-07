#!/usr/bin/env python3


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # simulate entire process,
        # try every path, if it cyle, not index with 0 in it, it not work

        # edge case, not val 0 in arr
        if min(arr) > 0:
            return False

        n = len(arr)

        def dfs(i, path):
            if i < 0 or i >= n:
                return False
            elif arr[i] == 0:
                return True
            elif i in path:
                return False
            else:
                path.add(i)
                return dfs(i + arr[i], path) or dfs(i - arr[i], path)

        return dfs(start, set())
