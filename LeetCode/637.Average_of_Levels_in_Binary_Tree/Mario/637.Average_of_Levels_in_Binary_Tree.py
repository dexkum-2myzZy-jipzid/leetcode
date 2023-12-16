#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
		res = []
		if not root:
			return res
		
		level_list = [root]
		while level_list:
			array = []
			sum_ = 0
			count = len(level_list)
			for node in level_list:
				sum_ += node.val
				if node.left:
					array.append(node.left)
				if node.right:
					array.append(node.right)
					
			res.append(sum_/count)
			level_list = array
			
		return res