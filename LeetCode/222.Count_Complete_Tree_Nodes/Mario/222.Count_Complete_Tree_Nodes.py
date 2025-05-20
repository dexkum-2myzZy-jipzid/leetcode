#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        if not root:
            return 0

        left_h = get_height(root.left)
        right_h = get_height(root.right)

        # print(f"left:{left_h} right:{right_h}")

        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            return (1 << right_h) + self.countNodes(root.left)
