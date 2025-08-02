#!/usr/bin/env python3


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # height[i] > suffix[i+1]
        n = len(heights)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], heights[i])

        res = []
        for i, h in enumerate(heights):
            if h > suffix[i + 1]:
                res.append(i)

        return res


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # height[i] > suffix[i+1]
        n = len(heights)
        res = []
        max_height = 0
        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return res[::-1]
