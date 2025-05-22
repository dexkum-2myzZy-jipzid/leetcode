#!/usr/bin/env python3


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bi -> ai
        # topological sort kahn algo

        # create graph based on prerequisite
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for p in prerequisites:
            a, b = p[0], p[1]
            graph[b].append(a)
            indegree[a] += 1

        # bfs
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        while q:
            e = q.popleft()
            res.append(e)

            for nei in graph[e]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []
