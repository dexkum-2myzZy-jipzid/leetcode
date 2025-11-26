#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        n = len(arr)

        left, right = 0, n - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]
