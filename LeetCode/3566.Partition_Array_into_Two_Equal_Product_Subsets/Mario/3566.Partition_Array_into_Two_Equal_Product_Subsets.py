#!/usr/bin/env python3


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        # dfs element has two choice

        def dfs(i, l, r):
            # print(f"i: {i} l:{l} r:{r}")
            if l > target or r > target or i > len(nums):
                return False

            if i == len(nums):
                if l == target and r == target:
                    return True
                else:
                    return False

            if l == target:
                return dfs(i + 1, l, r * nums[i])
            elif r == target:
                return dfs(i + 1, l * nums[i], r)
            else:
                return dfs(i + 1, l * nums[i], r) or dfs(i + 1, l, r * nums[i])

        return dfs(0, 1, 1)
