#!/usr/bin/env python3


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


# dfs
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            cp = Node(node.val)
            oldToNew[node] = cp
            for nei in node.neighbors:
                cp.neighbors.append(dfs(nei))
            return cp

        return dfs(node) if node else None


# bfs
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # create graph with adjacency list
        # handle edge case
        if not node:
            return None

        q = deque([node])
        copy = Node(node.val)

        dic = {node.val: copy}  # store copy nodes // val: node

        while q:
            cur = q.popleft()
            clone = dic[cur.val]

            for nei in cur.neighbors:
                if nei.val not in dic:
                    dic[nei.val] = Node(nei.val)
                    q.append(nei)
                clone.neighbors.append(dic[nei.val])

        return copy
