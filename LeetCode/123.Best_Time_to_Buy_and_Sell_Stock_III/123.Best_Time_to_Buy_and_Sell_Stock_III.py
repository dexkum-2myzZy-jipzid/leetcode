#!/usr/bin/env python3


# 两次遍历＋分段 DP的方法，不做状态压缩，来解决「最多两笔交易」的问题。
# 核心思路是把“最多两次交易”拆成“第一次交易”和“第二次交易”两部分，分别在数组的“左半段”与“右半段”计算各自的最大收益，然后枚举分割点。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first: 0 -> i, second: i+1 <- n-1

        # left array / right array

        # handle edge case
        if len(prices) < 2:
            return 0

        n = len(prices)

        left = [0] * n
        min_p = prices[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], prices[i] - min_p)
            min_p = min(min_p, prices[i])

        right = [0] * n
        max_p = prices[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], max_p - prices[i])
            max_p = max(max_p, prices[i])

        # print(f"left:{left} \t right:{right}")

        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i])

        return res


# 动态规划（DP）+状态压缩，将“交易次数”与“持股状态”编码进 DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        first: hold1 / sell1
        second: hold2 / selll2

        cur = prices[i]
        hold1 = max(pre_hold1, 0-cur)
        sell1 = max(pre_sell1, hold1 + cur)

        hold2 = max(pre_hold2, sell1-cur)
        sell2 = max(pre_sell2, hold2 + cur)
        """
        if len(prices) < 2:
            return 0

        hold1, sell1 = -prices[0], 0
        hold2, sell2 = -prices[0], 0

        for i in range(1, len(prices)):
            today = prices[i]

            sell2 = max(sell2, hold2 + today)
            hold2 = max(hold2, sell1 - today)

            sell1 = max(sell1, hold1 + today)
            hold1 = max(hold1, -today)

        return sell2


# multi dimensional dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][k][0/1]: i: ith day, k:transactions times (k <= 2),  0 /1 : hold stock or not

        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        """

        n = len(prices)
        k = 2

        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(k + 1):
            dp[0][i][1] = -prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                cur = prices[i]
                # no stock
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])

                # hold stock
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        # print(dp)

        return dp[n - 1][k][0]
