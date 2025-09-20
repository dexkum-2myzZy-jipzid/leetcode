#!/usr/bin/env python3


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(i):
            # print(nums)
            if i == n:
                res.append(nums[:])
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)

        return res
