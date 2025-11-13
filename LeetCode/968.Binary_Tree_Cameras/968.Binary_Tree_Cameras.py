#!/usr/bin/env python3

from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # min num of cameras
        # bottom up solution
        # every node
        # 3 states
        # not_covered, covered, with_camera

        @cache
        def dfs(node):
            if not node:
                return 0, 0, inf

            left = dfs(node.left)
            right = dfs(node.right)

            # not covered
            not_covered = left[1] + right[1]

            # covered
            covered = min(left[2] + right[1], left[1] + right[2], left[2] + right[2])

            # with_camera
            with_cam = min(left) + min(right) + 1

            return not_covered, covered, with_cam

        res = dfs(root)

        return min(res[1], res[2])


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        cover = {None}  # means

        def dfs(node: Optional[TreeNode], parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                # which case should be installed
                # 1. parent is None, node is uncovered
                # 2. left node is uncovered
                # 3. right node is uncovered
                if (
                    (parent is None and node not in cover)
                    or (node.left not in cover)
                    or (node.right not in cover)
                ):
                    self.res += 1

                    cover.update({parent, node, node.left, node.right})

        dfs(root)
        return self.res
