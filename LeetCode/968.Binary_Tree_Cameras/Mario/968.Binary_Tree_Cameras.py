#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
