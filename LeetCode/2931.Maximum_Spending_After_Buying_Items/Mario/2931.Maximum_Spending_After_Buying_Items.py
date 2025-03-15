#!/usr/bin/env python3

import heapq


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        # index of every row
        indices = [n - 1] * m

        heap = []
        # put last element into heap
        for i in range(m):
            heapq.heappush(heap, (values[i][n - 1], i, n - 1))

        day = 1
        res = 0

        while heap:
            val, row, col = heapq.heappop(heap)
            res += day * val
            day += 1
            # push rightmost available element
            col -= 1
            if col >= 0:
                newVal = values[row][col]
                heapq.heappush(heap, (newVal, row, col))

        return res


from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # Flatten the 2D list into a single list
        flattened = []
        for row in values:
            flattened.extend(row)

        # Sort the flattened list in ascending order
        flattened.sort()

        # Calculate the total spending
        total_spending = 0
        for day, value in enumerate(flattened, start=1):
            total_spending += day * value

        return total_spending
