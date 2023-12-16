#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		res = []
		if not root:
			return res
		
		level = [root]
		reverse = False
		while level:
			vals = []
			tmp = []
			for node in level:
				vals.append(node.val)
				if node.left:
					tmp.append(node.left)
				if node.right:
					tmp.append(node.right)
					
			if reverse:
				res.append(vals[::-1])
			else:
				res.append(vals)
			reverse = not reverse
			level = tmp
			
		return res