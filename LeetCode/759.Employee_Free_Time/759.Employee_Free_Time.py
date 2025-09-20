#!/usr/bin/env python3
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        # [1, 3] [4, 10]
        # free time slot: [-inf, 1], [3, 4], [10, inf]

        slots = []
        for intvls in schedule:
            for i in intvls:
                slots.append([i.start, i.end])

        sorted_slots = sorted(slots, key=lambda e: (e[0], e[1]))  # o(nlogn)

        # merge working time slots
        merge = []
        for e in sorted_slots:
            if not merge:
                merge.append(e)
            else:
                last = merge[-1]
                if last[1] < e[0]:
                    merge.append(e)
                else:
                    merge[-1] = [last[0], max(last[1], e[1])]

        # print(f"merge: {merge}")

        # check free time slots
        res = []
        for i in range(1, len(merge)):
            pre, cur = merge[i - 1], merge[i]
            # safe check
            if pre[1] < cur[0]:
                res.append(Interval(pre[1], cur[0]))

        return res


# k-way merge (heap)
class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        # k-way merge (heap)

        heap = []

        for i, lst in enumerate(schedule):
            if lst:
                first = lst[0]
                heapq.heappush(heap, (first.start, first.end, i, 0))
                # element in heap: (start time, end time, ith employee, jth time slots for ith employee)

        merged = []

        while heap:
            start, end, i, j = heapq.heappop(heap)

            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                last = merged[-1]
                merged[-1] = [last[0], max(last[1], end)]

            if j < len(schedule[i]) - 1:
                nxt = schedule[i][j + 1]
                heapq.heappush(heap, (nxt.start, nxt.end, i, j + 1))

        res = []
        for i in range(1, len(merged)):
            pre, cur = merged[i - 1], merged[i]
            if pre[1] < cur[0]:
                res.append(Interval(pre[1], cur[0]))

        return res
