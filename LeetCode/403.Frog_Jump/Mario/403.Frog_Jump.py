#!/usr/bin/env python3


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # may or not exist a stone
        # stones pos asecnding order
        # first jump 1 unit
        # last k, next k-1, k, k+1

        # 1 2 3 4 5 6 7  8
        # 0 1 3 5 6 8 12 17
        # 1 1.2 2   3 4  5
        # [0,1,2,3,4,8,9,11]

        # dp[i][j] = k, means i jump to j, previous max unit is k

        n = len(stones)
        dp = [[-1] * n for _ in range(n)]

        dic = defaultdict(int)
        for i, val in enumerate(stones):
            dic[val] = i

        k = 1
        # init dp
        if k in dic:
            dp[0][dic[k]] = 1
        else:
            # first jump can't reach any stone
            return False

        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j] == -1:
                    continue
                else:
                    k = dp[i][j]
                    val = stones[j]
                    for s in [k - 1, k, k + 1]:
                        if val + s in dic:
                            idx = dic[val + s]
                            dp[j][idx] = s

        res = False
        for i in range(n):
            if dp[i][n - 1] > 0:
                res = True

        return res


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # dp[i] = set(), contains k steps reach i
        n = len(stones)
        idx_map = {x: i for i, x in enumerate(stones)}

        dp = [set() for _ in range(n)]

        dp[0].add(0)

        for i in range(n):
            for k in dp[i]:
                for step in [k - 1, k, k + 1]:
                    if step <= 0:
                        continue
                    val = stones[i] + step
                    if val in idx_map:
                        j = idx_map[val]
                        dp[j].add(step)

        return len(dp[-1]) > 0
