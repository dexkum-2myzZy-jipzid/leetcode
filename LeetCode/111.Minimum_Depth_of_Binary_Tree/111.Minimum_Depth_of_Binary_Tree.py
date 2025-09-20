#!/usr/bin/env python3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if left is null
        if not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 如果树为空，深度为0
        if not root:
            return 0

        # 队列存储 (当前节点, 当前深度)
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # 如果是叶子节点，直接返回深度
            if not node.left and not node.right:
                return depth

            # 左子节点入队
            if node.left:
                queue.append((node.left, depth + 1))

            # 右子节点入队
            if node.right:
                queue.append((node.right, depth + 1))
