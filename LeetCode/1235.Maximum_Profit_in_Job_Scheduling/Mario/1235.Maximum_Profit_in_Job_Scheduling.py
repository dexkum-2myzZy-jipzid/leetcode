#!/usr/bin/env python3


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
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
