#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((root, 1))

        depth = 0
        while stack:
            node, cur_depth = stack.pop()
            if node:
                depth = max(depth, cur_depth)
                stack.append((node.left, cur_depth + 1))
                stack.append((node.right, cur_depth + 1))

        return depth
