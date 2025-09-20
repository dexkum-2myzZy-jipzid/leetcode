#!/usr/bin/env python3

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		if not digits:
			return []
		
		dic = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
		res = []
		
		def dfs(nums, letters):
			if not nums:
				res.append(letters)
			else:
				for a in dic[nums[0]]:
					dfs(nums[1:], letters+a)
					
		dfs(digits, "")
		return res  