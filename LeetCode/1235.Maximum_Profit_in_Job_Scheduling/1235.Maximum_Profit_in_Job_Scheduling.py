#!/usr/bin/env python3

import bisect
from functools import cache


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        # assume starttime is sorted
        n = len(startTime)
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append((s, e, p))

        jobs.sort()

        starts = [e[0] for e in jobs]
        ends = [e[1] for e in jobs]
        profits = [e[2] for e in jobs]

        next_job = []
        for i in range(n):
            idx = bisect.bisect_left(starts, ends[i])
            next_job.append(idx)

        @cache
        def dfs(i):
            if i >= n:
                return 0

            # not take
            res = dfs(i + 1)

            # take ith job
            return max(res, dfs(next_job[i]) + profits[i])

        return dfs(0)


# dp
class Solution2:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:

        # get jobs
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append((s, e, p))

        # sort jobs by endtime
        jobs.sort(key=lambda x: x[1])

        n = len(jobs)
        dp = [0] * n

        ends = [e for _, e, _ in jobs]

        for i, (s, e, p) in enumerate(jobs):
            # find jobs which endtime <= s
            j = bisect.bisect_right(ends, s) - 1
            # take current j jobs
            take = p + (dp[j] if j >= 0 else 0)
            # not take current j jobs
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(take, skip)

        return dp[n - 1]
