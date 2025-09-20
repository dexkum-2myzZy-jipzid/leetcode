#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # (row, cols), sort by cols, then row
        # traversal first, put position in the array, sort it
        # convert array to nested list
        arr = []

        def dfs(node, pos):
            if not node:
                return
            else:
                r, c = pos
                arr.append((c, r, node.val))
                # left
                dfs(node.left, (r + 1, c - 1))
                # right
                dfs(node.right, (r + 1, c + 1))

        dfs(root, (0, 0))
        arr.sort()
        res = []
        tmp = []
        for i in range(len(arr)):
            col, row, val = arr[i]
            if i > 0:
                pre = arr[i - 1][0]
                if col != pre:
                    res.append(tmp[:])
                    tmp = []
            tmp.append(val)

        res.append(tmp)
        return res
