#!/usr/bin/env python3

from math import inf


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dfs(ith stones, M) return stone

        n = len(piles)

        @cache
        def dfs(i, M, is_alice):
            if i >= n:
                return 0

            res = -inf if is_alice else inf
            stone = 0
            for j in range(i, i + 2 * M):  # [0, 2)
                if j >= n:
                    break
                stone += piles[j]
                NM = max(M, j - i + 1)
                val = stone if is_alice else -stone
                if is_alice:
                    res = max(res, dfs(j + 1, NM, not is_alice) + val)
                else:
                    res = min(res, dfs(j + 1, NM, not is_alice) + val)

            return res

        diff = dfs(0, 1, True)
        alice = (sum(piles) + diff) // 2

        return alice


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dfs(ith stones, M) return stone

        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        print(suffix_sum)

        @cache
        def dfs(i, M):
            if i >= n:
                return 0

            res = 0
            for X in range(1, 2 * M + 1):  # [1, 2 * M]
                if i + X > n:
                    break
                stone = suffix_sum[i] - suffix_sum[i + X]
                next_diff = dfs(i + X, max(M, X))
                res = max(res, stone + suffix_sum[i + X] - next_diff)

            return res

        return dfs(0, 1)
