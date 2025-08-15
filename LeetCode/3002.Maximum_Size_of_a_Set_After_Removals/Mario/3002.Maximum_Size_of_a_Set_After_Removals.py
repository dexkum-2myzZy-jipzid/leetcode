#!/usr/bin/env python3

from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        # max size of set s

        n = len(nums1)
        m = n // 2
        nums1, nums2 = set(nums1), set(nums2)

        duplicate_set = nums1 & nums2
        duplicate = len(duplicate_set)

        # count not duplicate num for nums1
        nums1 = min(len(nums1) - duplicate, n // 2)
        nums2 = min(len(nums2) - duplicate, n // 2)

        return min(nums1 + nums2 + duplicate, n)
