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
        n = len(piles)
        # 预处理后缀和
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0
            # 如果可以全部拿完
            if i + 2 * M >= n:
                return suffix_sum[i]
            # 枚举每种可能的取法
            res = 0
            for X in range(1, 2 * M + 1):
                # 拿X堆，对手接下来最多能拿 dp(i + X, max(M, X))
                res = max(res, suffix_sum[i] - dp(i + X, max(M, X)))
            return res

        return dp(0, 1)
