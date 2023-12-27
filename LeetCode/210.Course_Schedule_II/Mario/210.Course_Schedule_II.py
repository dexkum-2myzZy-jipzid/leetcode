#!/usr/bin/env python3

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        orders = []

        for array in prerequisites:
            a, b = array[0], array[1]
            preMap[a].append(b)

        cycle = set()
        visit = set()

        def dfs(course):
            if course in visit:
                return True

            if course in cycle:
                return False

            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            orders.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return orders
