#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # root is None
        if not root:
            return True

        def helper(p, q):
            # both none
            if not p and not q:
                return True
            # either none
            if not q or not p:
                return False
            # both not none
            if p.val != q.val:
                return False
            else:
                return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(root.left, root.right)
