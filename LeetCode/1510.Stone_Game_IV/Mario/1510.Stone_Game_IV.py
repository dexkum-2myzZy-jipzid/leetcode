#!/usr/bin/env python3


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # who can't move, who lost game
        # dp[0] = False

        # move options
        options = []
        k = 1
        while k * k <= n:
            options.append(k * k)
            k += 1

        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for stone in options:
                if stone > i:
                    break
                # alice lost, but if put bob in this position, alice win
                elif not dp[i - stone]:
                    dp[i] = True
                    break

        return dp[n]
