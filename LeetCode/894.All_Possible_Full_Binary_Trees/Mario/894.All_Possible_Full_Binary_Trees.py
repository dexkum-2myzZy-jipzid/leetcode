#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # full binary tree is a binary tree where each node has exactly 0 or 2 children.

        def build_FBT(start, end):
            # print(start, end)
            res = []
            if start == end:
                res.append(TreeNode(0))
                return res

            for i in range(start + 1, end, 2):
                # print(start, i, end)
                left = build_FBT(start, i - 1)
                right = build_FBT(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res

        return build_FBT(1, n)
