#!/usr/bin/env python3


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # dfs(i) ith request,
        # take i, count[i[0]] -= 1, count[i[1]] += 1, finally you count arry all = 0 means, store n
        # not take i
        m = len(requests)
        res = 0
        delta = [0] * n

        def dfs(i, cnt):
            nonlocal res, delta
            if i >= m:
                if all(d == 0 for d in delta):
                    res = max(res, cnt)
                return

            # not take i
            dfs(i + 1, cnt)

            # take i
            f, t = requests[i]
            delta[f] -= 1
            delta[t] += 1
            dfs(i + 1, cnt + 1)
            delta[f] += 1
            delta[t] -= 1

        dfs(0, 0)

        return res
