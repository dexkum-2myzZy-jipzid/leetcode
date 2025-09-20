#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {v: i for i, v in enumerate(inorder)}

        def helper(in_l, in_r, p_l, p_r):
            # base case
            if in_l > in_r or p_l > p_r:
                return None

            val = postorder[p_r]
            root = TreeNode(val)
            idx = dic[val]

            left_size = idx - in_l

            root.left = helper(in_l, idx - 1, p_l, p_l + left_size - 1)
            root.right = helper(idx + 1, in_r, p_l + left_size, p_r - 1)

            return root

        n = len(inorder)

        return helper(0, n - 1, 0, n - 1)
