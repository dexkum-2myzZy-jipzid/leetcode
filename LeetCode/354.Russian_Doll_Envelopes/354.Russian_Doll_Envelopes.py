#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))

        heights = [e[1] for e in envelopes]

        tails = []
        for h in heights:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)
