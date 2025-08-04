#!/usr/bin/env python3


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[i] = {k} represents set of possible step sizes to reach stone i
        # For each stone i and each step k in dp[i]:
        #   next_stones = stones[i] + (k-1), stones[i] + k, stones[i] + (k+1)
        #   if next_stone in stones: dp[stone_index[next_stone]].add(step_size)
        # Return len(dp[n-1]) > 0

        n = len(stones)
        idx_map = {s: i for i, s in enumerate(stones)}
        dp = [set() for _ in range(n)]
        dp[0] = {0}

        for i in range(n):
            cur = stones[i]
            for k in dp[i]:
                for dk in [-1, 0, 1]:
                    next_stone = cur + k + dk
                    if next_stone > cur and next_stone in idx_map:
                        dp[idx_map[next_stone]].add(k + dk)

        return len(dp[n - 1]) > 0


# dfs
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # k = 1, next_k in [k-1, k, k+1]
        # return if the frog can cross the river by landing on the last stone.
        # stones = [0,1,3,5,6,8,12,17]
        # stone: 0 -> 1 -> 3 -> 5 -> 8 -> 12 -> 17
        # unit:    1.   2.   2.   3.   4.    5

        # def dfs(i, j) 0, 1
        # three options:
        # stones[i] + j (j in [[k-1, k, k+1]]) in stones_idx_map
        # then dfs(next_i, j)
        # if next_i == n-1 return True

        n = len(stones)
        idx_map = {v: i for i, v in enumerate(stones)}

        @cache
        def dfs(i, j):
            # stone not in stones | frog must jump forward
            if i >= n or j <= 0:
                return False

            # reach last stone
            if i == n - 1:
                return True

            # next stone
            cur = stones[i] + j
            if cur not in idx_map:
                return False

            # 3 options
            for dj in [-1, 0, 1]:
                if dfs(idx_map[cur], j + dj):
                    return True

            return False

        return dfs(0, 1)
