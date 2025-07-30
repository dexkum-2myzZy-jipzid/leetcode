#!/usr/bin/env python3


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # max value of events you attented
        # dfs (last, ith)
        # not take ith: return previous value, not add it
        # take ith, make sure no conflict in event, then add value

        n = len(events)

        events.sort()

        # print(events)

        starts = [e[0] for e in events]
        ends = [e[1] for e in events]
        vals = [e[2] for e in events]

        next_event = []
        for i in range(n):
            idx = bisect.bisect_left(starts, ends[i] + 1)
            next_event.append(idx)

        @cache
        def dfs(i, k):
            # reach limit
            if k == 0 or i >= n:
                return 0

            # not take ith event
            res = dfs(i + 1, k)

            # take ith event
            return max(res, dfs(next_event[i], k - 1) + vals[i])

        return dfs(0, k)
