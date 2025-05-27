#!/usr/bin/env python3


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # task [actual, mini] actual:energy spend, mini energy to begin

        tasks.sort(key=lambda x: (-x[1] + x[0], x[1]))

        curr, init = 0, 0

        for spend, require in tasks:
            if curr < require:
                init += require - curr
                curr = require
            curr -= spend

        return init
