#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict, deque
from math import inf


class Solution:
    def specialNodes(
        self, n: int, edges: list[list[int]], x: int, y: int, z: int
    ) -> int:

        # build graph
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # get dx array: x to every other node distances
        def get_distance(i: int) -> list[int]:
            dist = [inf] * n
            dist[i] = 0
            q = deque([(0, i)])

            while q:
                d, node = q.popleft()

                for nei in tree[node]:
                    if d + 1 < dist[nei]:
                        dist[nei] = d + 1
                        q.append((d + 1, nei))

            return dist

        dx_arr, dy_arr, dz_arr = get_distance(x), get_distance(y), get_distance(z)

        res = 0
        for dx, dy, dz in zip(dx_arr, dy_arr, dz_arr):
            arr = [dx, dy, dz]
            arr.sort()
            a, b, c = arr
            if (a * a + b * b) == c * c:
                res += 1

        return res
