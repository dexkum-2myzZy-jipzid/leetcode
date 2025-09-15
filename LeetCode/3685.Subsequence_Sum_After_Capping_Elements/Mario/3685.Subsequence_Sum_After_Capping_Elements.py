#!/usr/bin/env python3


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        nums.sort()

        # 0/1 knapsack
        dp = [False] * (k + 1)
        dp[0] = True

        res = [False] * n

        # [1, 1, 1, 1]
        # [2, 2, 2, 2]
        # [2, 3, 3, 3]
        # [2, 3, 4, 4 ]
        # nums[left] < x , right >= x, all is x
        i = 0
        for x in range(1, n + 1):  # items for 0-1 knapsack
            # left side
            while i < n and nums[i] <= x:
                for j in range(k, nums[i] - 1, -1):
                    dp[j] = dp[j] or dp[j - nums[i]]
                i += 1

            # print(f"i:{i}\tx:{x}\ndp:{dp}")
            # right side, all val is x
            for j in range(min(n - i, k // x) + 1):
                if dp[k - j * x]:
                    res[x - 1] = True
                    break

        return res
