#!/usr/bin/env python3


# backtrack
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        res = []
        path = []

        def backtrack(i, total):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return

            for j in range(i, n):
                can = candidates[j]
                path.append(can)
                backtrack(j, total + can)
                path.pop()

        backtrack(0, 0)

        return res


# dp
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # dp[i] = []
        # dp[i] = dp[w - cand[i]] + [cand]

        # init dp
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for c in candidates:
            for j in range(c, target + 1):
                for e in dp[j - c]:
                    dp[j].append(e + [c])

        # print(dp)

        return dp[target]
