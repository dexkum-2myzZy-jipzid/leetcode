#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # sort nums
        # nums[i] + nums[i+1] > nums[i+2]

        nums.sort()

        n = len(nums)

        for i in range(n - 1, 1, -1):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if a + b > c:
                return a + b + c

        return 0


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # heapify this nums,
        # because i want to make it max heap, so negative all element in nums
        # [2,1,2] => [-2, -1, -2]

        # then pop 2 element, a, b
        # c is top of element, heap[0]
        # if b + c > a: it means form triangle, it larget perimeter
        # return
        # if not, push(-b) into heap,

        heap = [-num for num in nums]
        heapq.heapify(heap)

        while len(heap) >= 3:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            c = -heap[0]

            if b + c > a:
                return a + b + c
            else:
                heapq.heappush(heap, -b)

        return 0
