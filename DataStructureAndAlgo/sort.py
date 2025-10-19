#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quick Sort
"""

import random


def quick_sort(nums: list[int]):

    def partition(left: int, right: int) -> int:
        pivot = nums[random.randint(left, right)]
        i, j = left, right
        while True:
            # find nums[i] >= pivot
            while nums[i] < pivot:
                i += 1

            # find nums[j] <= pivot
            while nums[j] > pivot:
                j -= 1

            # nums[left..i-1] <= pivot && piovt >= nums[j+1, right]
            if i >= j:
                return j

            # swap
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def sort(left: int, right: int):
        if left < right:
            p = partition(left, right)
            sort(left, p)
            sort(p + 1, right)

    sort(0, len(nums) - 1)
    return nums


"""
Merge Sort
"""


def merge_sort(nums: list[int]) -> list[int]:
    tmp = [0] * len(nums)

    def sort(left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2
        sort(left, mid)
        sort(mid + 1, right)

        # early exit
        if nums[mid] <= nums[mid + 1]:
            return

        l, r = left, mid + 1
        i = l
        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                tmp[i] = nums[l]
                l += 1
            else:
                tmp[i] = nums[r]
                r += 1
            i += 1

        # handle rest part
        while l <= mid:
            tmp[i] = nums[l]
            i += 1
            l += 1

        while r <= right:
            tmp[i] = nums[r]
            i += 1
            r += 1

        nums[left : right + 1] = tmp[left : right + 1]

    sort(0, len(nums) - 1)
    return nums


if __name__ == "__main__":
    nums1 = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    nums3 = [-1, 2, -8, -10]
    nums4 = [-2, 3, -5]
    nums5 = [110, 100, 0]

    print("-" * 20 + "quick sort" + "-" * 20)
    print(quick_sort(nums1))
    print(quick_sort(nums2))
    print(quick_sort(nums3))
    print(quick_sort(nums4))
    print(quick_sort(nums5))

    nums1 = [5, 2, 3, 1]
    nums2 = [5, 1, 1, 2, 0, 0]
    nums3 = [-1, 2, -8, -10]
    nums4 = [-2, 3, -5]
    nums5 = [110, 100, 0]

    print("-" * 20 + "merge sort" + "-" * 20)
    print(merge_sort(nums1))
    print(merge_sort(nums2))
    print(merge_sort(nums3))
    print(merge_sort(nums4))
    print(merge_sort(nums5))
