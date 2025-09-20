#!/usr/bin/env python3
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if len(s) == 0:
            return None

        n = len(s)

        # break s into root, left, right
        stack = []  # store '(' index
        left_first, left_last = -1, -1
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) == 1:
                    left_first = stack.pop()
                    left_last = i
                    break
                stack.pop()

        if left_first == -1:
            left_first = n

        root = TreeNode(int(s[:left_first]))
        left_str = right_str = ""
        if left_last != -1:
            left_str = s[left_first + 1 : left_last]
            right_str = s[left_last + 2 : -1]

        root.left = self.str2tree(left_str)
        root.right = self.str2tree(right_str)

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        # node(left)(right)

        if not s:
            return None

        n = len(s)

        # return node, index
        def helper(idx):
            if idx >= n:
                return None, idx

            sign = 1
            if s[idx] == "-":
                sign = -1
                idx += 1

            num = 0
            while idx < n and s[idx].isdigit():
                num = num * 10 + int(s[idx])
                idx += 1
            node = TreeNode(num * sign)

            # left tree
            if idx < n and s[idx] == "(":
                idx += 1
                node.left, idx = helper(idx)
                idx += 1  # skip ')'

            # right tree
            if idx < n and s[idx] == "(":
                idx += 1
                node.right, idx = helper(idx)
                idx += 1  # skip ')'

            return node, idx

        return helper(0)[0]
