#!/usr/bin/env python3


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) >> 1
            if mid + 1 < n and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


class Solution2:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if mid == len(arr) - 1:
                right = mid
                continue

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
