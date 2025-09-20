#!/usr/bin/env python3

from collections import defaultdict
from typing import List
import heapq
from math import inf


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijstra algo
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dis = [inf] * (n + 1)
        dis[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)

            for nei, w in graph[u]:
                if d + w < dis[nei]:
                    dis[nei] = d + w
                    heapq.heappush(heap, (d + w, nei))

        res = max(dis[1:])

        return res if res != inf else -1
