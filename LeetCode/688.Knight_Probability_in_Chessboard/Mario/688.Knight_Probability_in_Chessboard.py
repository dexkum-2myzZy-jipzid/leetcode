#!/usr/bin/env python3


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # n * n chessboard
        # Return the probability that the knight remains on the board after it has stopped moving.

        # evey move has 8 options, prob (keep board count) / 8
        # dp = [set() for _ in range(k)]

        # handle edge case
        DIRS = [
            (2, 1),
            (1, 2),
            (-2, -1),
            (-1, -2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (-1, 2),
        ]

        dp = [defaultdict(float) for _ in range(k + 1)]

        # init dp
        dp[0][(row, column)] = 1.0

        for i in range(1, k + 1):
            for key in dp[i - 1]:
                r, c = key
                p = dp[i - 1][key]
                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < n and 0 <= nc < n:
                        np = p * (1 / 8)
                        if (nc, nr) in dp[i]:
                            dp[i][(nc, nr)] += np
                        else:
                            dp[i][(nc, nr)] = np

        # print(dp)

        res = 0
        for key in dp[k]:
            r, c = key
            p = dp[k][key]
            res += p

        return res
