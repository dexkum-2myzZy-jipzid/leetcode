#!/usr/bin/env python3


class SegmentTree:
    def __init__(self, data):
        """
        初始化线段树
        :param data: 待处理的列表（数组），索引从 0 开始
        """
        self.n = len(data)
        # 预留足够空间，4 * n 通常足够
        self.tree = [0] * (4 * self.n)
        self.data = data[:]  # 保存一份原始数据的拷贝
        self._build(0, self.n - 1, 1)

    def _build(self, start, end, idx):
        """
        递归建树，将 data[start...end] 的信息存入 tree[idx] 中
        :param start: 当前区间的左边界
        :param end: 当前区间的右边界
        :param idx: 当前节点在 tree 中的编号(根节点编号为 1)
        """
        if start == end:
            self.tree[idx] = self.data[start]
            return
        mid = (start + end) // 2
        # 递归建造左右子树
        self._build(start, mid, idx * 2)
        self._build(mid + 1, end, idx * 2 + 1)
        # 当前节点的值为左右子节点的和
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def query(self, l, r):
        """
        查询区间 [l, r] 的和
        :param l: 查询区间左端(0-based)
        :param r: 查询区间右端
        :return: 区间内所有数的和
        """
        return self._query(0, self.n - 1, l, r, 1)

    def _query(self, start, end, l, r, idx):
        # 当前区间完全在查询区间内
        if l <= start and end <= r:
            return self.tree[idx]
        mid = (start + end) // 2
        res = 0
        # 若左侧子区间与查询区间有交集
        if l <= mid:
            res += self._query(start, mid, l, r, idx * 2)
        # 若右侧子区间与查询区间有交集
        if r > mid:
            res += self._query(mid + 1, end, l, r, idx * 2 + 1)
        return res

    def update(self, pos, value):
        """
        更新数组中下标 pos 的元素为 value
        :param pos: 要更新的数组下标(0-based)
        :param value: 更新后的新值
        """
        self._update(0, self.n - 1, pos, value, 1)

    def _update(self, start, end, pos, value, idx):
        # 到达叶子节点，更新值
        if start == end:
            self.tree[idx] = value
            self.data[pos] = value
            return
        mid = (start + end) // 2
        if pos <= mid:
            self._update(start, mid, pos, value, idx * 2)
        else:
            self._update(mid + 1, end, pos, value, idx * 2 + 1)
        # 更新当前节点的值
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]


# 示例使用
if __name__ == "__main__":
    # 初始数组
    arr = [1, 3, 5, 7, 9, 11]
    seg = SegmentTree(arr)

    # 查询区间 [1, 3] 的和
    print("初始区间和 [1,3]:", seg.query(1, 3))  # 输出 3 + 5 + 7 = 15

    # 更新下标 2 的元素（原值 5）为 6
    seg.update(2, 6)
    print("更新后区间和 [1,3]:", seg.query(1, 3))  # 3 + 6 + 7 = 16
