#!/usr/bin/env python3

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        # print(intervals)
        q_idx = sorted([(q, i) for i, q in enumerate(queries)])
        heap = []  # min heap
        i = 0  # for intervals

        res = [0] * len(queries)

        # print(f"q_idx:{q_idx}\n")

        for q, j in q_idx:
            # push start time of interval <= q into heap
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e))
                i += 1

            # print(heap)
            # heap pop end time of interval < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            res[j] = heap[0][0] if heap else -1

        return res
