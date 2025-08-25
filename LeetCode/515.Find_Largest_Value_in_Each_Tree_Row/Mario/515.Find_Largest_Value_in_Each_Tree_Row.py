#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from math import inf


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            size = len(q)
            max_val = -inf
            for _ in range(size):
                cur = q.popleft()
                max_val = max(max_val, cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(max_val)

        return res
