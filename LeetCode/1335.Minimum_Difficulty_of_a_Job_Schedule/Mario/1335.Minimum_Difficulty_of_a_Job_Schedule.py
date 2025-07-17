#!/usr/bin/env python3


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # constraints:
        # [0, i-1] -> i job
        # at least one task every day
        # divide jobdiff arr into d segments

        # min sum(d days)
        # dp[i][k] sum diff schedule previous i jobs, assign k days

        n = len(jobDifficulty)
        dp = [[inf] * (d + 1) for _ in range(n + 1)]

        # init dp
        dp[0][0] = 0

        for k in range(1, d + 1):
            for i in range(k, n + 1):
                # cur_d = jobDifficulty[i]
                max_d = 0

                # check k-1 days max diff job
                for j in range(i - 1, k - 2, -1):  # [k-1, i-1]
                    max_d = max(max_d, jobDifficulty[j])
                    if dp[j][k - 1] != inf:
                        dp[i][k] = min(dp[i][k], dp[j][k - 1] + max_d)

        # for row in dp:
        #     print(row)

        return dp[n][d] if dp[n][d] != inf else -1
