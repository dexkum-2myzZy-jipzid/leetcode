#!/usr/bin/env python3

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        m = max(nums)
        tree = [0] * (4 * m)

        def update(start, end, pos, val, idx):
            if start == end:
                tree[idx] = val
                return
            mid = (start + end) // 2
            if pos <= mid:
                update(start, mid, pos, val, 2 * idx)
            else:
                update(mid + 1, end, pos, val, 2 * idx + 1)
            tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])

        def query(start, end, l, r, idx):
            if l <= start and end <= r:
                return tree[idx]
            res = 0
            mid = (start + end) // 2
            if l <= mid:
                res = query(start, mid, l, r, 2 * idx)
            if r > mid:
                res = max(res, query(mid + 1, end, l, r, 2 * idx + 1))
            return res

        for num in nums:
            if num == 1:
                update(1, m, 1, 1, 1)
            else:
                res = 1 + query(1, m, max(num - k, 1), num - 1, 1)
                update(1, m, num, res, 1)

        return tree[1]
