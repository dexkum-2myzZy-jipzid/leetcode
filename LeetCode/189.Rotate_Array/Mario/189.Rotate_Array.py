#!/usr/bin/env python3


# 189. Rotate Array
# three reverse
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[: n - k] = nums[: n - k][::-1]
        nums[n - k :] = nums[n - k :][::-1]
        nums[:] = nums[::-1]


# 环状替换（Cyclic Replacements）
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0 or n == 0:
            return

        start, count = 0, 0
        while count < n:
            cur = start
            cur_val = nums[start]
            while True:
                nxt = (cur + k) % n
                nums[nxt], cur_val = cur_val, nums[nxt]
                count += 1
                cur = nxt
                if cur == start:
                    break
            start += 1
