#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res = inf

        def dfs(node):
            nonlocal res
            if not node:
                return

            if abs(node.val - target) < abs(res - target):
                res = node.val
            elif abs(node.val - target) == abs(res - target) and node.val < res:
                res = node.val

            if res == target:
                return

            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)

        return res
