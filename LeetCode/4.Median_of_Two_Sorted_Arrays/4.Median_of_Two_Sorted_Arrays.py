#!/usr/bin/env python3


from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # why swap
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)  # 3, 3 total = 6, half = 3
        total = m + n
        half = (total + 1) // 2  # why add 1

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left = nums1[i - 1] if i - 1 >= 0 else -inf
            nums1_right = nums1[i] if i < m else inf
            nums2_left = nums2[j - 1] if j - 1 >= 0 else -inf
            nums2_right = nums2[j] if j < n else inf

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # odd
                max_left = max(nums1_left, nums2_left)
                if total % 2 == 1:
                    return float(max_left)
                else:
                    # even
                    min_right = min(nums1_right, nums2_right)
                    return float(max_left + min_right) / 2.0

            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
