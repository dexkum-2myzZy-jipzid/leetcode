#!/usr/bin/env python3


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ensure nums1 is a shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        left, right = 0, m  # left, right for nums1
        half = (m + n + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = half - i

            if i < m and nums1[i] < nums2[j - 1]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return maxLeft

                # get minRight
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                return (maxLeft + minRight) / 2.0
