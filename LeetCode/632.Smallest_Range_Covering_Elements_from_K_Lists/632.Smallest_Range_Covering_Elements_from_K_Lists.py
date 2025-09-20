#!/usr/bin/env python3


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        heap = []
        right = -math.inf

        for i, lst in enumerate(nums):
            val = lst[0]
            heapq.heappush(heap, (val, i, 0))  # (val, row_index, column_index)
            right = max(right, val)

        res = [-(10**5), 10**5]

        while heap:
            (val, i, j) = heapq.heappop(heap)

            if right - val < res[1] - res[0]:
                res = [val, right]

            if j + 1 == len(nums[i]):
                break

            next_val = nums[i][j + 1]
            right = max(right, next_val)
            heapq.heappush(heap, (next_val, i, j + 1))

        return res
