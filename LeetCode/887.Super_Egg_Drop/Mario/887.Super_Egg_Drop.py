#!/usr/bin/env python3


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[m][k]: m 次操作，k 个鸡蛋，最多能测试多少层
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        m = 0
        while dp[m][k] < n:
            m += 1
            for eggs in range(1, k + 1):
                dp[m][eggs] = dp[m - 1][eggs - 1] + dp[m - 1][eggs] + 1
        return m
