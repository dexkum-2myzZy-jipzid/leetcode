#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # [root] + [left boundary] + [leaves] + [right boundary]

        res = []
        if root:
            res.append(root.val)

        def left_bounadry(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            else:
                res.append(node.val)
                if node.left:
                    left_bounadry(node.left)
                elif node.right:
                    left_bounadry(node.right)

        right = []

        def right_bounadry(node):
            if not node:
                return
            if not node.left and not node.right:
                return
            else:
                right.append(node.val)
                if node.right:
                    right_bounadry(node.right)
                elif node.left:
                    right_bounadry(node.left)

        def pre_travseral(node):
            if not node:
                return

            if not node.left and not node.right and node != root:
                res.append(node.val)
                return

            left = pre_travseral(node.left)
            right = pre_travseral(node.right)

        if root.left:
            left_bounadry(root.left)

        pre_travseral(root)
        if root.right:
            right_bounadry(root.right)

        # print(res)
        # print(right)

        return res + right[::-1]
