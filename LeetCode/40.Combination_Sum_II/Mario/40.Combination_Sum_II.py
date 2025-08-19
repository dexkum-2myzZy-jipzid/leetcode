#!/usr/bin/env python3


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidate and filter it, if cand > target, impossible conbination
        # [1, 1, 2, 5, 6, 7]

        cands = sorted(candidates)
        cands = [v for v in cands if v <= target]
        n = len(cands)
        # print(cands)
        res = []

        def backtrack(i, path, remaining):
            # valid case
            if remaining == 0:
                res.append(path[:])
                return

            # invalid case
            if i >= n:
                return

            for j in range(i, n):
                cur = cands[j]
                if j > i and cands[j] == cands[j - 1]:
                    continue
                if cur > remaining:
                    break
                path.append(cur)
                backtrack(j + 1, path, remaining - cur)
                path.pop()

        backtrack(0, [], target)

        return res
