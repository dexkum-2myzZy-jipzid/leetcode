#!/usr/bin/env python3


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 1 vertical / hori
        # vert:left, hor:up
        # Return the number of ways of cutting the pizza such that each piece contains at least one apple.

        # dfs(i, j, k)
        # cut i in [i+1, n-1]
        # cut j in [j+1, n-1]

        # count apple

        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        count = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apple = 1 if pizza[i][j] == "A" else 0
                for di, dj in [(1, 0), (0, 1)]:
                    ni, nj = i + di, j + dj
                    apple += count[ni][nj]
                apple -= count[i + 1][j + 1]
                count[i][j] = apple

        # for r in count:
        #     print(r)

        @cache
        def dfs(i, j, k):
            if k < 0 or i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if k == 0 and count[i][j] > 0:
                return 1

            total = count[i][j]
            ways = 0
            # horizontal cut
            for ii in range(i + 1, m):
                cur = count[ii][j]
                if total - cur > 0 and cur > 0:
                    ways = (ways + dfs(ii, j, k - 1)) % MOD

            # vertical cut
            for jj in range(j + 1, n):
                cur = count[i][jj]
                if total - cur > 0 and cur > 0:
                    ways = (ways + dfs(i, jj, k - 1)) % MOD

            return ways

        return dfs(0, 0, k - 1)
