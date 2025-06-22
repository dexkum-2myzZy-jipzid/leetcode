#!/usr/bin/env python3


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 3 subarrays
        # max sum
        # res indice
        # sum[i] the sum of length k subarray
        # [3,3,3,8,13,12,6]

        n = len(nums)
        sums = []

        # 1. prefix sum,
        l = 0
        sub = 0
        for r, num in enumerate(nums):
            sub += num
            if (r - l + 1) == k:
                sums.append(sub)
                sub -= nums[l]
                l += 1

        m = len(sums)

        left = [0] * m
        max_left = 0
        for i in range(m):
            if sums[i] > sums[max_left]:
                max_left = i
            left[i] = max_left

        right = [0] * m
        max_right = m - 1
        for i in range(m - 1, -1, -1):
            if sums[i] >= sums[max_right]:
                max_right = i
            right[i] = max_right

        # print(f"sums: {sums}")
        # print(f"left: {left}")
        # print(f"right: {right}")

        # a, b, c
        res = [-1, -1, -1]
        total = 0
        for b in range(k, m - k):
            a, c = left[b - k], right[b + k]
            new_total = sums[a] + sums[b] + sums[c]
            if new_total > total:
                res = [a, b, c]
                total = new_total

        return res
