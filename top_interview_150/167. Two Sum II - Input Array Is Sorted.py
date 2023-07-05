#!/usr/bin/env python3

# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            ans = numbers[i] + numbers[j]
            if ans > target:
                j -= 1
            elif ans < target:
                i += 1
            else:
                return [i+1, j+1]
