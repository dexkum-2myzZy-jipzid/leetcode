#!/usr/bin/env python3


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b]: b -> a
        # build graph, directed graph,
        # toplogical sort - khan algo

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
