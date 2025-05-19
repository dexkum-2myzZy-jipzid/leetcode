#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, val):
            if not root:
                return 0

            val = val * 10 + root.val
            # leaf
            if not root.left and not root.right:
                return val

            return dfs(root.left, val) + dfs(root.right, val)

        return dfs(root, 0)
