#!/usr/bin/env python3


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # dp[i][j]: means max diff score palyer1 can get over player2 in nums[i:j]

        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i, num in enumerate(nums):
            dp[i][i] = num

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                else:
                    dp[i][j] = max(
                        nums[i] - dp[i + 1][j],  # take left side
                        nums[j] - dp[i][j - 1],  # take right side
                    )
        # print(dp)
        return dp[0][n - 1] >= 0
