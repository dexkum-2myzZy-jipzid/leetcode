#!/usr/bin/env python3

import heapq


class RecentCounter:

    def __init__(self):
        self.heap = []

    def ping(self, t: int) -> int:
        while self.heap and t - self.heap[0] > 3000:
            heapq.heappop(self.heap)
        heapq.heappush(self.heap, t)
        return len(self.heap)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
