#!/usr/bin/env python3


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-based 索引

    def update(self, i, delta):
        # i 是更新的位置（从1开始）
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # 找到下一个需要更新的位置

    def query(self, i):
        # 查询前缀和 [1..i]
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)  # 跳到父节点
        return res

    def range_query(self, l, r):
        # 查询区间和 [l..r]
        return self.query(r) - self.query(l - 1)
