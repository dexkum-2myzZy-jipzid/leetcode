#!/usr/bin/env python3


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # pick up k-1 times max(nums[i]+nums[i+1]) / min(nums[i]+nums[i+1])
        # top k-1 questions
        n = len(weights)
        if k == 1 or k == n:
            return 0

        arr = []
        for i in range(n - 1):
            arr.append(weights[i] + weights[i + 1])

        arr.sort()

        minScore = sum(arr[: k - 1])
        maxScore = sum(arr[-(k - 1) :])

        return maxScore - minScore
