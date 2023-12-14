#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		self.res = root.val
		
		def dfs(node):
			if not node:
				return 0
			
			rightMax = dfs(node.right)
			leftMax = dfs(node.left)
			leftMax = max(leftMax, 0)
			rightMax = max(rightMax, 0)
			
			self.res = max(self.res, node.val+leftMax+rightMax)
			
			return node.val + max(leftMax, rightMax)
		
		dfs(root)
		return self.res