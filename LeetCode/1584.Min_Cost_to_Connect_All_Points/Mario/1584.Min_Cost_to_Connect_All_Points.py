#!/usr/bin/env python3
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # check whether ith point in the MST
        inMST = set()
        # store distance bwteen point to MST
        minDist = [math.inf] * n
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
