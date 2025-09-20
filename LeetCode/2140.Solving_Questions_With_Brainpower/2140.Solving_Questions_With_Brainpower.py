#!/usr/bin/env python3


# dfs
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
        # 0: get 3 pt, can't solve 1 & 2
        # 1: get 4 pt, can't solve 2 & 3

        # dfs i, return points,
        # solve ith proble dfs(i + q[i][1] + 1) + point

        n = len(questions)

        @cache
        def dfs(i):
            if i >= n:
                return 0

            # solve ith question
            point, power = questions[i]
            solve = dfs(i + power + 1) + point

            # skip
            skip = dfs(i + 1)

            return max(solve, skip)

        return dfs(0)


# dp
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # reverse dp
        # dp[i]
        # skip dp[i] = dp[i+1]
        # solve: dp[i] = dp[i+brainpower+1] + points
        # return dp[0]

        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            point, power = questions[i]

            # solve
            nxt = min(i + power + 1, n)
            take = dp[nxt] + point

            # skip
            not_take = dp[i + 1]

            dp[i] = max(take, not_take)

        return dp[0]
