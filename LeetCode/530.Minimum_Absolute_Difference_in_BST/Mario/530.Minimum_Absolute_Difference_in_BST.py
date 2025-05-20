#!/usr/bin/env python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # for every node, compare node - left most max / node - right min val
        self.res = math.inf
        self.prev = None

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            if self.prev is not None:
                # print(f"prev:{self.prev} current:{root.val}")
                self.res = min(self.res, abs(self.prev - root.val))
            self.prev = root.val

            inorder(root.right)

        inorder(root)

        return self.res
