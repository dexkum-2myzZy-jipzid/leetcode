#!/usr/bin/env python3


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # tiring day hours > 8
        # the days of tiring days > the days of no-tiring days

        n = len(hours)
        prefix = [0]
        for h in hours:
            prefix.append(prefix[-1] + (1 if h > 8 else -1))
        # print(prefix)

        seen = defaultdict(int)
        res = 0
        for i, val in enumerate(prefix):

            if val > 0:
                res = max(res, i)
            elif val - 1 in seen:
                res = max(res, i - seen[val - 1])

            if val not in seen:
                seen[val] = i

        return res
