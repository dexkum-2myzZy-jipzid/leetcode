#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        if n == 1 or n == 3:
            return False
        elif n == 2:
            return True

        dp[2] = True
        prev_loss = [1, 3]

        for i in range(4, n + 1):
            m = len(prev_loss)
            for j in range(m):
                x = i - prev_loss[j]
                if i % x == 0:
                    dp[i] = True
                    break
            if not dp[i]:
                prev_loss.append(i)

        return dp[n]


class Solution2:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
