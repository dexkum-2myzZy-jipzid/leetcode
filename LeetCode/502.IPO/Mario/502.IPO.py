#!/usr/bin/env python3


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # profits[i] profit you can get, capital[i] you needed to start
        n = len(profits)
        # greedy, choose biggest profits <= w
        # two heap
        # 1. min heap, sort by capital
        # 2. max heap, sort by profits

        heap = list(zip(capital, profits))

        heapq.heapify(heap)
        max_heap = []  # (profits, capital)

        for _ in range(k):

            while heap and heap[0][0] <= w:
                c, p = heapq.heappop(heap)
                heapq.heappush(max_heap, -p)

            if max_heap:
                neg_p = heapq.heappop(max_heap)
                w += -neg_p
            else:
                break

        return w
