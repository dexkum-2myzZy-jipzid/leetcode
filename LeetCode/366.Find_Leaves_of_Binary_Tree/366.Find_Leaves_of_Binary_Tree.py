#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        # pre-order traversal this binary tree
        # if node left and right all None, means this is leaf
        # push it into global array
        # also, i will remove this node, return None
        self.res = []

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            if node.left is None and node.right is None:
                self.res.append(node.val)
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            node.left = left
            node.right = right

            return node

        ans = []
        curr = root
        while curr:
            curr = dfs(curr)
            ans.append(self.res)
            self.res = []

        return ans


class Solution2:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def dfs(node: Optional[TreeNode]) -> int:
            # the height of leaves == 0
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            height = max(left, right) + 1

            if height == len(res):
                res.append([])

            res[height].append(node.val)

            return height

        dfs(root)

        return res
