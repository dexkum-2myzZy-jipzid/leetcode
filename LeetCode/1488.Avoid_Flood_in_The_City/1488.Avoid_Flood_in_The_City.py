#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from collections import defaultdict, deque


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)

        indices = defaultdict(deque)
        for i, rain in enumerate(rains):
            if rain > 0:
                indices[rain].append(i)

        # lakers which are full of water
        water = set()
        heap = []  # (next_index, laker)
        res = [-1] * n

        for i, rain in enumerate(rains):
            if rain > 0:

                indices[rain].popleft()

                # laker is full of water, rain again flood now
                if rain in water:
                    return []

                water.add(rain)

                if indices[rain]:
                    next_idx = indices[rain][0]
                    heapq.heappush(heap, (next_idx, rain))
            else:

                if heap:
                    next_idx, lake = heapq.heappop(heap)
                    res[i] = lake
                    water.remove(lake)
                else:
                    res[i] = 1

        return res
