#!/usr/bin/env python3


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i, n0 in enumerate(nums):
            if n0 > 0:
                break
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s > -n0:
                    k -= 1
                elif s < -n0:
                    j += 1
                else:
                    res.append([n0, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res
