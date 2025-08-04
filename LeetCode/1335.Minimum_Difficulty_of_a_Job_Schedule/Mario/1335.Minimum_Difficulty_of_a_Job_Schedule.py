#!/usr/bin/env python3


from math import inf


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # at least 1 task/day, diff = max(jobs in a day)
        # min diff,not return -1

        # dp[i][j] represents min difficulty when first i jobs scheduled in j days
        # For each possible last day starting position k:
        #   dp[i][j] = min(dp[k-1][j-1] + max(jobsDiff[k:i+1])) for all valid k
        # where max(jobsDiff[k:i+1]) is the difficulty of day j (jobs from k to i)

        n = len(jobDifficulty)

        dp = [[inf] * (d + 1) for _ in range(n + 1)]

        # 0th day, 0 job min dff = 0
        dp[0][0] = 0

        # ith job
        for i in range(1, n + 1):
            # jth day
            for j in range(1, min(i, d) + 1):
                maxd = 0

                # last jth, we can scheduled[j-1,i] jobs
                # because j-1 jobs must be scheduled j-1 days
                # one pass backward
                for k in range(i, j - 2, -1):
                    maxd = max(maxd, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + maxd)

        return dp[n][d] if dp[n][d] != inf else -1
