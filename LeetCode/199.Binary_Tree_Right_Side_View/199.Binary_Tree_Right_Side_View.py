#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        level = [root]

        while level:
            rightMostValue = 0
            array = []
            for node in level:
                rightMostValue = node.val
                if node.left:
                    array.append(node.left)
                if node.right:
                    array.append(node.right)
            res.append(rightMostValue)
            level = array

        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            # right first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return res
