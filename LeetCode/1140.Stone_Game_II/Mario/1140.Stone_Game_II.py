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
