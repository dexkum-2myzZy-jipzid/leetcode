#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # bfs
        q = deque([root])
        res = []

        while q:
            size = len(q)
            sum0 = 0
            for i in range(size):
                cur = q.popleft()
                sum0 += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(sum0 / size)

        return res
