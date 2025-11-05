#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    SEP = ","
    NIL = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append(self.NIL)
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.SEP.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        arr = data.split(self.SEP)
        self.i = 0

        def build():
            if self.i >= len(arr):
                return None

            val = arr[self.i]
            self.i += 1
            if val == self.NIL:
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node

        return build()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
