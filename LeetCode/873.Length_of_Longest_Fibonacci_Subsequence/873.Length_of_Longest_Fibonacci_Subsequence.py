#!/usr/bin/env python3


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # dp[i][j]
        # if arr[k] = arr[i] + arr[j]
        # dp[j][k] = max(dp[j][k], dp[i][j] + 1)

        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        idx_map = {val: i for i, val in enumerate(arr)}

        # init dp
        for i in range(n):
            dp[i][i] = 1

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                val = arr[j] - arr[i]
                if val < arr[i] and val in idx_map:
                    k = idx_map[val]
                    dp[i][j] = max(dp[i][j], dp[k][i] + 1)
                    res = max(res, dp[i][j])

        # for r in dp:
        #     print(r)

        return res
