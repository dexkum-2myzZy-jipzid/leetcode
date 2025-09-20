#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        # return (is_bst or not, sum, smallest val, biggest val)
        def dfs(root):
            if not root:
                return True, 0, inf, -inf

            l_bst, l_sum, l_small, l_large = dfs(root.left)
            r_bst, r_sum, r_small, r_large = dfs(root.right)

            cur_bst = (l_large < root.val < r_small) and l_bst and r_bst

            cur_sum = 0
            if cur_bst:
                cur_sum = root.val + l_sum + r_sum
                self.res = max(self.res, cur_sum)
                return cur_bst, cur_sum, min(l_small, root.val), max(r_large, root.val)
            else:
                return cur_bst, cur_sum, inf, -inf

        dfs(root)

        return self.res
