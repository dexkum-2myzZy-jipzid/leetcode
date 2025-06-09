#!/usr/bin/env python3


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        # [1, 3, 6, 8] 5

        nums.sort()
        sums = [nums[0]]

        for i in range(1, n):
            sums.append(sums[-1] + nums[i])

        # print(sums)
        res = []
        for q in queries:
            # test case
            ops = 0
            if q >= nums[-1]:
                ops = q * n - sums[-1]
            elif q <= nums[0]:
                ops = sums[-1] - q * n
            else:
                i = bisect.bisect_left(nums, q)
                # print(i)
                left_sum = sums[i - 1]  # small than q
                right_sum = sums[-1] - left_sum  # bigger than q
                ops = i * q - left_sum
                ops += right_sum - q * (n - i)

            res.append(ops)

        return res
