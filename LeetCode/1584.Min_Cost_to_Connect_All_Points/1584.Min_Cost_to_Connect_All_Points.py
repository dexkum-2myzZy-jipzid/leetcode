#!/usr/bin/env python3
import heapq
from typing import List
from math import inf


# MST - Kruskal
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # check whether ith point in the MST
        inMST = set()
        # store distance bwteen point to MST
        minDist = [inf] * n
        # heap store vertex
        heap = [(0, 0)]

        res = 0
        while heap and len(inMST) < n:
            w, v = heapq.heappop(heap)
            if v in inMST:
                continue
            # sum distance between nodes
            res += w

            # store v in the inMST set
            inMST.add(v)

            a, b = points[v][0], points[v][1]
            for i, p in enumerate(points):
                if i not in inMST:
                    x, y = p[0], p[1]
                    dist = abs(x - a) + abs(y - b)
                    if dist < minDist[i]:
                        minDist[i] = dist
                        heapq.heappush(heap, (dist, i))

        return res


# MST - Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_cost = [inf] * n
        in_MST = [False] * n

        # init
        min_cost[0] = 0

        res = 0
        for _ in range(n):
            u, best = -1, inf
            for i in range(n):
                if not in_MST[i] and min_cost[i] < best:
                    best, u = min_cost[i], i

            # add vertex u into MST
            in_MST[u] = True
            res += best

            # relax: update all points which not in MST
            x, y = points[u]
            for v in range(n):
                if not in_MST[v]:
                    a, b = points[v]
                    dis = abs(a - x) + abs(b - y)
                    if dis < min_cost[v]:
                        min_cost[v] = dis

        return res
