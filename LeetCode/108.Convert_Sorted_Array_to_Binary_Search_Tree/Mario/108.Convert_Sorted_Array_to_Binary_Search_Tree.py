#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def numsToBST(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])

            mid = (l + r) // 2
            left = numsToBST(l, mid - 1)
            right = numsToBST(mid + 1, r)

            node = TreeNode(nums[mid])
            node.left, node.right = left, right
            return node

        return numsToBST(0, len(nums) - 1)
