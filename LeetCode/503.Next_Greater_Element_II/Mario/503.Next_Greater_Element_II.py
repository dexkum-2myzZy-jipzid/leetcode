#!/usr/bin/env python3


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # greater = [-1] * n store next greater for num

        n = len(nums)
        greater = [-1] * n
        i = 0
        stack = []  # monotonic stack contains num's index by no-increasing order

        while i < 2 * n:
            idx = i if i < n else i - n
            cur = nums[idx]

            while stack and nums[stack[-1]] < cur:
                lastIdx = stack.pop()
                greater[lastIdx] = cur

            if i < n:
                stack.append(idx)
            i += 1

        return greater
