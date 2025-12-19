#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from collections import defaultdict, deque


class Solution:
    def sequenceReconstruction(
        self, nums: List[int], sequences: List[List[int]]
    ) -> bool:
        # 1->2, 1->3, 2->3

        # E = sum(len(seq)-1 for seq in sequences)
        # V = len(nums)

        # topological sort
        n = len(nums)
        graph = defaultdict(list)
        indegree = [0] * n

        # O(E)
        for lst in sequences:
            if len(lst) < 2:
                continue
            for i in range(len(lst) - 1):
                a, b = lst[i], lst[i + 1]
                graph[a].append(b)
                indegree[b - 1] += 1

        # O(V)
        queue = deque([i + 1 for i, val in enumerate(indegree) if val == 0])

        res = []

        # O(V + E)
        while queue:
            if len(queue) != 1:
                return False

            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei - 1] -= 1
                if indegree[nei - 1] == 0:
                    queue.append(nei)

        return res == nums
