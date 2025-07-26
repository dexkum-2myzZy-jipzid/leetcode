#!/usr/bin/env python3


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # comb = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     comb[i][0] = 1
        #     for j in range(1, i+1):
        #         comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

        def dfs(nodes):
            n = len(nodes)

            if len(nodes) < 2:
                return 1

            left = [x for x in nodes if x < nodes[0]]
            right = [x for x in nodes if x > nodes[0]]

            left_ways = dfs(left)
            right_ways = dfs(right)

            return (math.comb(n - 1, len(left)) * left_ways * right_ways) % MOD

        return dfs(nums) - 1
