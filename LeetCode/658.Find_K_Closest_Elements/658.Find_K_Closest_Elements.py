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


class Solution2:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:

        # a[mid],a[mid+1],....,a[mid+k-1]
        #        a[mid+1],.....,a[mid+k-1], a[mid+k]
        # [a[mid]...  x. ... a[mid+k]]
        # x - a[mid] < a[mid+k] - x

        n = len(arr)

        left, right = 0, n - k - 1
        while left <= right:
            mid = (left + right) // 2

            if x - arr[mid] <= arr[mid + k] - x:
                right = mid - 1
            else:
                left = mid + 1

        return arr[left : left + k]
