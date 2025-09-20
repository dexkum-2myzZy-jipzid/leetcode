#!/usr/bin/env python3


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = inf
        for s, t in tasks:
            res = min(res, s + t)
        return res
