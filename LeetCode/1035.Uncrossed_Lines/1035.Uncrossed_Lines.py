#!/usr/bin/env python3


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # max lines
        # dp[i][j] means nums1[:i] nums2[:j] max lines
        # if nums1[i] == nums[j]:  dp[i][j] = dp[i][j] + 1
        # if not: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # nums1 = [1,4,2],
        # nums2 = [1,2,4]
        # 1, 0, 0
        # 0, 0, 1
        # 0, 1, 0

        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
