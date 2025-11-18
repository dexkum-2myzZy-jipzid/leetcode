#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        # 1. odd: [0, 1, 2, 3, 4] mid = 2 (0, 4)
        #     left, mid-1, / mid, right-1
        # 2. even: [0, 1, 2, 3] mid = 1 (0, 3)
        #     left, mid / mid +1, right

        n = reader.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            odd = (right - left + 1) % 2 == 1
            if odd:
                l, r, x, y = left, mid - 1, mid, right - 1
            else:
                l, r, x, y = left, mid, mid + 1, right
            res = reader.compareSub(l, r, x, y)
            if res == 1:
                left, right = l, r
            elif res == -1:
                left, right = x, y
            else:
                if odd:
                    return right

        return left
