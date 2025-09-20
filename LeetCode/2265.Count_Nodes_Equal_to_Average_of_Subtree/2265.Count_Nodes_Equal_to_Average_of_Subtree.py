#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        # dfs input node sum count
        # return (sum, count)
        def dfs(node):
            if not node:
                return (0, 0)

            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)

            count = lc + rc + 1
            acc = ls + rs + node.val

            if node.val == acc // count:
                self.res += 1

            # print(f"acc:{acc} count:{count}")
            return (acc, count)

        dfs(root)
        return self.res
