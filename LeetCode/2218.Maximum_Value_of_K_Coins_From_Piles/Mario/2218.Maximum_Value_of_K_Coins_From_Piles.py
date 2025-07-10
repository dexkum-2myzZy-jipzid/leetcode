#!/usr/bin/env python3


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [0] * (k + 1)
        for pile in piles:
            prefix_sum = [0]
            for coin in pile:
                prefix_sum.append(prefix_sum[-1] + coin)
            # Update dp in reverse order (0-1 knapsack)
            for j in range(k, 0, -1):
                for x in range(1, min(len(prefix_sum), j + 1)):
                    dp[j] = max(dp[j], dp[j - x] + prefix_sum[x])
        return dp[k]


#
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [
            [0] * (k + 1) for _ in range(n + 1)
        ]  # dp[i][j]: first i piles, take j coins

        for i in range(1, n + 1):
            pile = piles[i - 1]

            prefix_sum = [0]
            for coin in pile:
                prefix_sum.append(prefix_sum[-1] + coin)

            for j in range(k + 1):
                for x in range(0, min(len(pile), j) + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + prefix_sum[x])

        # print(dp)
        return dp[n][k]
