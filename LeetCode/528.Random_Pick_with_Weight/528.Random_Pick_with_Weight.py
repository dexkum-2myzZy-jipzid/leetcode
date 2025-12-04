#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.prefix.append(w[0])
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])

    def pickIndex(self) -> int:
        val = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, val)
        return idx
