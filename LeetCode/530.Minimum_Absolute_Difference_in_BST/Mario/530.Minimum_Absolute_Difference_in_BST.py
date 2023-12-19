#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        array = []

        def dfs(node):
            if node:
                dfs(node.left)
                array.append(node.val)
                dfs(node.right)

        dfs(root)
        minDiff = float('inf')
        for i in range(len(array)-1):
            minDiff = min(minDiff, array[i+1]-array[i])

        return minDiff
