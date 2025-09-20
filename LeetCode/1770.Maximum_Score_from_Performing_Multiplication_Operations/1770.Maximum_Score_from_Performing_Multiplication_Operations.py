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


# dfs
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n, m = len(nums), len(multipliers)

        # i:left, j:right
        @cache
        def dfs(i, j):
            k = i + j
            if k >= m:
                return 0

            mul = multipliers[k]

            # take left
            left = dfs(i + 1, j) + nums[i] * mul

            # take right
            right = dfs(i, j + 1) + nums[-(j + 1)] * mul

            return max(left, right)

        return dfs(0, 0)
