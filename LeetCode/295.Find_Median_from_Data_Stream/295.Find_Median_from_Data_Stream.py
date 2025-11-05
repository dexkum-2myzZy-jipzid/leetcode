#!/usr/bin/env python3
import heapq


class MedianFinder:

    # heap, max heap, min heap
    # arr = [2,3,4]
    # low = [-2] # max heap (negative)
    # high = [3, 4] # min heap

    def __init__(self):
        self.low, self.high = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # balance, make sure len(self.high) == (len(self.low) or len(self.low) + 1)
        if len(self.high) > len(self.low) + 1:
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        n = len(self.low) + len(self.high)
        if n % 2 == 1:
            return float(self.high[0])
        else:
            return float(-self.low[0] + self.high[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
