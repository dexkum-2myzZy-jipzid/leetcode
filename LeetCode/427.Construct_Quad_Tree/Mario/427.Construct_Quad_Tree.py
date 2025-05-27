#!/usr/bin/env python3

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        # divide and conquer
        # x: row, y: col
        def build(xi, yi, xj, yj):
            if xi > xj or yi > yj:
                return None

            is_leaf = True
            val = grid[xi][yj]
            for i in range(xi, xj + 1):
                for j in range(yi, yj + 1):
                    if val != grid[i][j]:
                        is_leaf = False
                        break
                if is_leaf == False:
                    break

            if not is_leaf:
                x = (xi + xj) // 2
                y = (yi + yj) // 2

                top_l = build(xi, yi, x, y)
                top_r = build(xi, y + 1, x, yj)
                bottom_l = build(x + 1, yi, xj, y)
                bottom_r = build(x + 1, y + 1, xj, yj)

                return Node(is_leaf, is_leaf, top_l, top_r, bottom_l, bottom_r)
            else:
                return Node(bool(val), is_leaf, None, None, None, None)

        n = len(grid)
        return build(0, 0, n - 1, n - 1)
