#!/usr/bin/env python3


# binary search + difference array
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # nums, queries
        # return minimum k, first k queries

        # how to minus val in range: difference array
        # binary search

        n, m = len(nums), len(queries)

        def is_zero(k):
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                diff[r + 1] -= v

            total = 0
            for i, num in enumerate(nums):
                total += diff[i]
                if num > total:
                    return False
            return True

        res = inf
        left, right = 0, m
        while left <= right:
            mid = (left + right) >> 1
            # print(f"mid:{mid}\tleft:{left}\tright:{right}\tres:{res}")
            if is_zero(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res if res != inf else -1


# line sweep
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total = k = 0
        diff = [0] * (n + 1)

        for i in range(n):

            while total + diff[i] < nums[i]:
                k += 1

                # zero array is impossible
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # update diff
                if right >= i:
                    diff[max(left, i)] += val
                    diff[right + 1] -= val

            total += diff[i]

        return k
