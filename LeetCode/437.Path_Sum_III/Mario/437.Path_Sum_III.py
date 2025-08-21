#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(
            node, prefix_dic, prefixsum
        ):  # dictionary key:prefixsum: cnt, prefixsum
            nonlocal res
            # base case:
            if not node:
                return

            new_prefixsum = prefixsum + node.val
            if new_prefixsum - targetSum in prefix_dic:
                res += prefix_dic[new_prefixsum - targetSum]
            prefix_dic[new_prefixsum] += 1

            # go further subtree
            dfs(node.left, prefix_dic, new_prefixsum)
            dfs(node.right, prefix_dic, new_prefixsum)

            prefix_dic[new_prefixsum] -= 1

        dic = defaultdict(int)
        dic[0] = 1
        dfs(root, dic, 0)

        return res
