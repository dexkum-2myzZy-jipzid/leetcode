#!/usr/bin/env python3

from collections import defaultdict, deque
from typing import List


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        # idea: topological sort for group and items in group

        # 0. build graph for groups and items
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1

        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)
        group_items = defaultdict(list)

        for i in range(n):
            group_items[group[i]].append(i)
            for pre in beforeItems[i]:
                # in same group, means items in group graph
                if group[pre] == group[i]:
                    item_graph[pre].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[group[pre]].append(group[i])
                    group_indegree[group[i]] += 1

        # 1. group top sort first
        def top_sort(nodes, graph, indegree):
            res = []
            q = deque([node for node in nodes if indegree[node] == 0])
            while q:
                node = q.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return res if len(res) == len(nodes) else []

        all_group_ids = list(set(group))
        group_order = top_sort(all_group_ids, group_graph, group_indegree)
        if not group_order:
            return []

        # 2. items in group top sort
        res = []
        for g in group_order:
            items = group_items[g]
            items_order = top_sort(items, item_graph, item_indegree)
            if not items_order:
                return []
            res.extend(items_order)
        return res
