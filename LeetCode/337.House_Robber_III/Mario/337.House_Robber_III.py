#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs return two state, one is not rob, one is rob

        def dfs(node):
            if not node:
                return (0, 0)  # rob, not rob

            left = dfs(node.left)
            right = dfs(node.right)

            # rob
            rob = left[1] + node.val + right[1]
            # not rob
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))
