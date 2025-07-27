#!/usr/bin/env python3


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # num, k
        # divide nums into k subsets, every sum of subset is n
        # backtrack

        total = sum(nums)
        if total % k != 0:
            return False

        n = len(nums)
        target = total // k
        seen = [False] * n

        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        # ith num, k buckets, current sum of bucket
        def dfs(i, k, cur_sum):
            # all buckets filled
            if k == 0:
                return True

            if cur_sum == target:
                return dfs(0, k - 1, 0)

            for j in range(i, n):
                if not seen[j] and cur_sum + nums[j] <= target:
                    seen[j] = True
                    if dfs(j + 1, k, cur_sum + nums[j]):
                        return True
                    seen[j] = False

                    # Pruning: If placing this number in an empty bucket fails, return False
                    if cur_sum == 0:
                        return False

            return False

        return dfs(0, k, 0)
