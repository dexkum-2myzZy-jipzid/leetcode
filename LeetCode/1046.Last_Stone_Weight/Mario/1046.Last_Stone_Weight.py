#!/usr/bin/env python3

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            diff = abs(y - x)
            if diff > 0:
                heapq.heappush(heap, -diff)

        return 0 if not heap else -heapq.heappop(heap)
