#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = left + right + node.val
            count[subtree_sum] += 1
            max_freq = max(max_freq, count[subtree_sum])

            return subtree_sum

        dfs(root)
        res = []
        for k in count:
            if count[k] == max_freq:
                res.append(k)

        return res
