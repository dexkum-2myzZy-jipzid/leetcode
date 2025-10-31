#!/usr/bin/env python3

import heapq
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # using monotonic stack, store decreasing array,
        # when meet a number is bigger than last element of stack,
        # it means that format a place can trap water

        stack = []
        n = len(height)
        res = 0  # how much water trap
        for i, h in enumerate(height):

            while stack and height[stack[-1]] < h:
                bottom = height[stack.pop()]
                if not stack:
                    break
                left = stack[-1]
                minH = min(height[left], h) - bottom
                res += minH * (i - left - 1)

            stack.append(i)

        return res


# heap & bfs
class Solution2:
    def trap(self, height: List[int]) -> int:
        # heap + bfs
        n = len(height)

        # edge case
        if n < 3:
            return 0

        heap = []
        visited = [False] * n
        for i in [0, n - 1]:
            heapq.heappush(heap, (height[i], i))
            visited[i] = True

        res = 0
        DIRS = [-1, 1]
        while heap:
            cur, i = heapq.heappop(heap)

            for di in DIRS:
                ni = di + i
                if 0 <= ni < n and not visited[ni]:
                    trap_water = max(0, cur - height[ni])
                    res += trap_water

                    visited[ni] = True
                    heapq.heappush(heap, (max(cur, height[ni]), ni))

        return res


# two pointers
class Solution3:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max = right_max = 0
        water = 0

        # for each position,  min(left_max, right_max) - current_height

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
