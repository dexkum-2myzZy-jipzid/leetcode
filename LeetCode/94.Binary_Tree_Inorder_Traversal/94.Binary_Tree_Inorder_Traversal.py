#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        res = []

        while node or stack:
            if not node:
                last = stack.pop()
                res.append(last.val)
                node = last.right
            else:
                if node.left:
                    stack.append(node)
                    node = node.left
                else:
                    res.append(node.val)
                    node = node.right

        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        res = []

        while node or stack:
            # go to leftmost node
            while node:
                stack.append(node)
                node = node.left

            # visit node
            last = stack.pop()
            res.append(last.val)

            # go to right child
            node = last.right

        return res
