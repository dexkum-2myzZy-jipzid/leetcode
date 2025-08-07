#!/usr/bin/env python3

from math import inf


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            if len(lis) == idx:
                lis.append(num)
            else:
                lis[idx] = num
        return len(lis) >= 3


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # first < num <= second
                second = num
            else:
                # num > second > first
                return True

        return False
