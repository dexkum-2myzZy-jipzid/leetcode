#!/usr/bin/env python3


class Solution:
    def numSquares(self, n: int) -> int:
        # ps = perfectsquare
        # dp[i] = min(dp[i-ps]) for ps in ps array

        dp = [inf] * (n + 1)
        dp[0] = 0

        # get array contains perfect square num
        ps = []
        for i in range(1, n + 1):
            if i * i <= n:
                ps.append(i * i)
            else:
                break

        # print(ps)

        for i in range(1, n + 1):
            for p in ps:
                if i - p >= 0:
                    dp[i] = min(dp[i], dp[i - p] + 1)

        return dp[n]


# BFS + greedy
class Solution:
    def numSquares(self, n: int) -> int:
        # get list contains perfect square nums

        ps = [i * i for i in range(1, int(n**0.5) + 1)]

        q = deque([n])
        vis = {n}
        step = 0

        while q:
            step += 1
            size = len(q)

            for _ in range(size):
                val = q.popleft()

                for p in ps:
                    tmp = val - p
                    if tmp < 0:
                        break
                    elif tmp == 0:
                        return step

                    if tmp not in vis:
                        vis.add(val - p)
                        q.append(val - p)

        return -1
