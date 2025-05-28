#!/usr/bin/env python3


# bisect_left
def bisect_left(nums, target):
    n = len(nums)
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if target <= nums[m]:
            r = m
        else:
            l = m + 1
    return l


# bisect_right
def bisect_right(nums, target):
    n = len(nums)
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if target < nums[m]:
            r = m
        else:
            l = m + 1
    return l
