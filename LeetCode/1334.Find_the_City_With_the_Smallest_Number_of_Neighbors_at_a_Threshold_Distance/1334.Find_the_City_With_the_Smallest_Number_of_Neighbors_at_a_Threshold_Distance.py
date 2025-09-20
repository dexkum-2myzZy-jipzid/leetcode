#!/usr/bin/env python3

from typing import List
from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # n cities, [0, n-1]
        # edges bidirectional
        # at most threshold

        dis = [[inf] * n for _ in range(n)]

        for i in range(n):
            dis[i][i] = 0

        for u, v, w in edges:
            dis[u][v] = w
            dis[v][u] = w

        # main Floyd Warshall
        for k in range(n):
            for i in range(n):
                dik = dis[i][k]
                if dik == inf:
                    continue
                for j in range(n):
                    if dis[k][j] != inf:
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        min_count = inf
        res = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and dis[i][j] <= distanceThreshold:
                    cnt += 1

            if cnt <= min_count:
                min_count = cnt
                res = i

        return res
