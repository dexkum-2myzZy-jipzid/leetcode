#!/usr/bin/env python3


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # the number of left part is (n+m+1) // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left = (n + m + 1) // 2

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = left - i

            nums1_left = nums1[i - 1] if i > 0 else -math.inf
            nums1_right = nums1[i] if i < m else math.inf
            nums2_left = nums2[j - 1] if j > 0 else -math.inf
            nums2_right = nums2[j] if j < n else math.inf

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (
                        max(nums1_left, nums2_left) + min(nums1_right, nums2_right)
                    ) / 2.0
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
