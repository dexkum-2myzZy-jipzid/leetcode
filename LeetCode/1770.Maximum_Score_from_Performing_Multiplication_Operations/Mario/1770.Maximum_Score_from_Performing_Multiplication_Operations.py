#!/usr/bin/env python3


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        dp = [[-inf] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            y = multipliers[i - 1]
            for left in range(i + 1):
                right = i - left

                # choose start
                if left > 0:
                    dp[i][left] = max(
                        dp[i][left], dp[i - 1][left - 1] + nums[left - 1] * y
                    )

                # choose end
                if right > 0:
                    dp[i][left] = max(dp[i][left], dp[i - 1][left] + nums[-right] * y)

        return max(dp[m][j] for j in range(m + 1) if dp[m][j] != -inf)
