#!/usr/bin/env python3


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) >> 1
            if mid + 1 < n and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
