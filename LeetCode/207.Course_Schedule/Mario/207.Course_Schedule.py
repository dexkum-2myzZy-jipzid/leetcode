#!/usr/bin/env python3

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertexs = []
        edges = {}

        for prerequisite in prerequisites:
            course, pre = prerequisite[0], prerequisite[1]
            vertexs.append(course)
            if course in edges:
                edges[course].append(pre)
            else:
                edges[course] = [pre]

        visit = set()

        def dfs(vertex):
            if vertex not in edges:
                return True

            # has cycle
            if vertex in visit:
                return False

            visit.add(vertex)
            for val in edges[vertex]:
                if not dfs(val):
                    return False
            visit.remove(vertex)
            edges[vertex] = []
            return True

        for v in vertexs:
            if not dfs(v):
                return False
        return True
