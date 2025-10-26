#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def can_split_into_k(m: int) -> bool:
            cnt, cur = 1, 0
            for num in nums:
                cur += num
                if cur <= m:
                    continue
                else:
                    cur = num
                    cnt += 1
                    if cnt > k:
                        return False
            return True

        left, right = max(nums), sum(nums) + 1
        while left < right:
            mid = (left + right) // 2
            if can_split_into_k(mid):
                right = mid
            else:
                left = mid + 1

        return left
