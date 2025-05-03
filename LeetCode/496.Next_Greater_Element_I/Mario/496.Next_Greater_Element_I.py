#!/usr/bin/env python3


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # get nextGreaterElement for nums2
        # stack = [] store index,
        # if hit num which <= nums2[stack[-1]], stack.append(i)
        # else while

        greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                last = stack.pop()
                greater[last] = num

            stack.append(num)

        # print(f"greater: {greater}")

        res = []
        for i, num in enumerate(nums1):
            val = -1 if num not in greater else greater[num]
            res.append(val)

        return res
