#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))

    def helper(self, root, min, max):
        if not root:
            return True
        if min >= root.val or max <= root.val:
            return False
        res = self.helper(root.left, min, root.val) and self.helper(
            root.right, root.val, max)
        return res
