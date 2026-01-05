#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import inf
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        # edge case
        if src == dst:
            return 0

        min_dis = [inf] * n
        min_dis[src] = 0

        for i in range(k + 1):
            tmp = min_dis[:]
            updated = False
            for from_city, to_city, price in flights:
                # relax
                if (
                    min_dis[from_city] != inf
                    and min_dis[from_city] + price < tmp[to_city]
                ):
                    tmp[to_city] = min_dis[from_city] + price
                    updated = True

            min_dis = tmp
            # print(min_dis)
            if not updated:
                break

        # ensure return type is int
        if min_dis[dst] != inf:
            return int(min_dis[dst])
        else:
            return -1


# Dijkstra algo
class Solution2:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for v, u, p in flights:
            graph[v].append((u, p))

        heap = [(0, src, 0)]
        best = [[inf] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while heap:
            price, curr, stops = heapq.heappop(heap)

            if curr == dst:
                return price

            # more than k stops, cut off branch
            if stops >= k + 1:
                continue

            for nei, p in graph[curr]:
                nprice = price + p
                nstops = stops + 1
                if best[nei][nstops] > nprice:
                    best[nei][nstops] = nprice
                    heapq.heappush(heap, (nprice, nei, nstops))

        return -1


class Solution3:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for v, u, p in flights:
            graph[v].append((u, p))

        heap = [(0, 0, src)]
        best = [inf] * n
        best[src] = 0

        while heap:
            price, stops, curr = heapq.heappop(heap)

            if curr == dst:
                return price

            # more than k stops, cut off branch
            if stops > k or stops > best[curr]:
                continue

            best[curr] = stops

            for nei, p in graph[curr]:
                nprice = price + p
                heapq.heappush(heap, (nprice, stops + 1, nei))

        return -1
