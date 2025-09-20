#!/usr/bin/env python3

import heapq
from typing import List


class KthLargest:
    # [2,3, 4,5,8] k = 3 4
    # min_heap the length this heap is k
    # add val, compare val with the top element, if > top, heap pop, push val
    # if not, return heap[0]

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
