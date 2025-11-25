#!/usr/bin/env python3

from typing import List


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


class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # binary search
        # missing number

        # [1, 2, 5] k= 2. 5-3= 2

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing_num = arr[mid] - (mid + 1)
            if missing_num < k:
                left = mid + 1
            else:
                right = mid - 1

        # left = right+1
        # kth missing in arr[right] and arr[left]
        # arr[right] - (right+1)
        # arr[right] + k - arr[right] + (right+1) = k + right + 1

        return left + k
