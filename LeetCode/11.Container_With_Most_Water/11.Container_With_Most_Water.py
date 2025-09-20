#!/usr/bin/env python3


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            water = h * (j - i)
            max_water = max(max_water, water)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return max_water
