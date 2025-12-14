#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        # dfs
        # seen: hold ids which has already visited

        # dict: id:employee
        dic = {e.id: e for e in employees}

        def dfs(eid: int) -> int:
            if eid not in dic:
                return 0

            employee = dic[eid]

            total = employee.importance
            for eid in employee.subordinates:
                total += dfs(eid)

            return total

        return dfs(id)
