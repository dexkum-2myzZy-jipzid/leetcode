#!/usr/bin/env python3


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # [a, b] b-a = diff
        #  dp = [0] * (max(arr) + 1)
        #  val + diff

        dp = defaultdict(int)
        res = 0

        for i, val in enumerate(arr):
            pre = val - difference
            if pre not in dp:
                dp[val] = 1
            else:
                dp[val] = max(dp[val], dp[pre] + 1)
            res = max(res, dp[val])

        # print(dp)

        return res
