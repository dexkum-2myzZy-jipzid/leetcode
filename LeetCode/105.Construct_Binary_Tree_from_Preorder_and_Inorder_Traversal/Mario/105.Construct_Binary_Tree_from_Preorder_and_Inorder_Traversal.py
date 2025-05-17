#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {val: i for i, val in enumerate(inorder)}

        def helper(pre_l, pre_r, in_l, in_r):
            # base case
            if pre_l > pre_r:
                return None

            val = preorder[pre_l]
            root = TreeNode(val)

            idx = dic[val]
            left_size = idx - in_l

            root.left = helper(pre_l + 1, pre_l + left_size, in_l, idx - 1)
            root.right = helper(pre_l + 1 + left_size, pre_r, idx + 1, in_r)

            return root

        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)
