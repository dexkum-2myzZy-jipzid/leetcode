#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # sweep line
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        max_room = current_room = 0
        events.sort()

        for time, delta in events:
            current_room += delta
            max_room = max(max_room, current_room)

        return max_room


class Solution2:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
