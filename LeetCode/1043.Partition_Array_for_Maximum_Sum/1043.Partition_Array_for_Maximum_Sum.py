#!/usr/bin/env python3

from functools import cache


# dfs
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # largest sum
        # 25 * (10^4) * k
        # divide arr into diff segments following rule at most k

        # def dfs(pre_max, ith, remaning_k)
        n = len(arr)

        @cache
        def dfs(pre_max, i, j):
            if i == n:
                return pre_max * (k - j)

            # start new segment
            res = dfs(arr[i], i + 1, k - 1) + pre_max * (k - j)

            if j != 0:
                # using remaining k
                res = max(res, dfs(max(arr[i], pre_max), i + 1, j - 1))

            return res


# dp
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dp[i] represents max sum of arr[:i]
        #  for length in range(2, min(i, k) + 1):
        #       j = i+1 - length
        #       max_val = max(arr[j:i])
        # . dp[i] = max_val * length + dp[j-1]

        n = len(arr)
        dp = [0] * n

        # init dp
        dp[0] = arr[0]

        for i in range(1, n):
            max_val = arr[i]
            for length in range(1, min(i + 1, k) + 1):
                j = i - length + 1
                # print(f"i:{i}\tj:{j}")
                max_val = max(max_val, arr[j])
                dp[i] = max(dp[i], max_val * length + (0 if j == 0 else dp[j - 1]))

        # print(dp)
        return dp[-1]
