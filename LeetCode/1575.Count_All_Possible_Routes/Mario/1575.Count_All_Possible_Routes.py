#!/usr/bin/env python3


class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        # location[i] = city i
        # if i, pick j, i != j
        # fuel = abs(loca[i] - loca[j])
        # fule [1, 200]

        # [2,3,6,8,4]
        # . 0,1,2,3,4
        # 3 -> 8

        # dp[fuel][i] count of routes start from i city with fuel

        # dp[fuel][i] = for j in locations: next_fuel = abs(location[i] - locations[j]) dp[next_fuel][j]

        MOD = 10**9 + 7
        n = len(locations)
        dp = [[0] * n for _ in range(fuel + 1)]

        # init dp
        dp[0][start] = 1

        for f in range(fuel + 1):
            for i in range(n):
                if dp[f][i] > 0:
                    for j, loc in enumerate(locations):
                        if i == j:
                            continue
                        else:
                            need_f = abs(locations[i] - loc)
                            if (f + need_f) <= fuel:
                                dp[f + need_f][j] = (dp[f + need_f][j] + dp[f][i]) % MOD

        # for r in dp:
        #     print(dp)

        res = 0
        for f in range(fuel + 1):
            res = (res + dp[f][finish]) % MOD

        return res
