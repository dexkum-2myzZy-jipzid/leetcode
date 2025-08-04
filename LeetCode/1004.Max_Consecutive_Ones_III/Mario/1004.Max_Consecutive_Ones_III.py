#!/usr/bin/env python3


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window,
        # l, r
        # sum(nums[l:r]) = how many 1s
        # sum + k >= (l -r + 1)
        # res = max(l - r + 1, res)

        # if sum + k > (l - r +1):
        # expand
        # if sum + k < (l - r + 1)
        # shrink
        l = count = 0

        res = 0
        for i, num in enumerate(nums):
            count += num
            # [l, i] zeros > ones, so have to shrink
            while count + k < (i - l + 1):
                count -= nums[l]
                l += 1
            res = max(res, i - l + 1)

        return res
