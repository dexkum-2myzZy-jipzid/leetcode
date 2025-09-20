#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b]: b -> a
        # build graph, directed graph,
        # topological sort - kahn algo 卡恩

        indegree = [0] * numCourses
        graph = defaultdict(list)
        for pre in prerequisites:
            a, b = pre[0], pre[1]  # b -> a / b -> c
            indegree[a] += 1
            graph[b].append(a)

        q = deque()
        for i, num in enumerate(indegree):
            if num == 0:
                q.append(i)

        while q:
            cur = q.popleft()

            if cur in graph:
                for v in graph[cur]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

        return sum(indegree) == 0


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # bi -> ai
        n = numCourses

        indegree = [0] * n
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            i = q.popleft()

            for nei in graph[i]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return all(e == 0 for e in indegree)
