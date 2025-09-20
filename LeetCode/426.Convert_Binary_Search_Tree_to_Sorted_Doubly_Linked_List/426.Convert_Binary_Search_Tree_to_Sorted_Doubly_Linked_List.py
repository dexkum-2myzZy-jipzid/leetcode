#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        # binary search tree
        # small -> big
        # inorder
        if not root:
            return root

        first, last = None, None

        def dfs(node):
            nonlocal first, last
            # base case
            # node == None
            if not node:
                return

            dfs(node.left)

            # node how to connect, create linked list
            if not first and not last:
                first = last = node
            elif last:
                last.right = node
                node.left = last
                last = node

            dfs(node.right)

        dfs(root)
        first.left = last
        last.right = first

        return first
