#!/usr/bin/env python3

from typing import List


# linear traversal
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # increasing order, k
        num = 0
        i = 0
        while k > 0:
            num += 1
            if i < len(arr) and num == arr[i]:
                i += 1
            else:
                k -= 1

        return num


# binary search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) >> 1
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid

        return left + k
