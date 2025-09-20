#!/usr/bin/env python3


# segment tree:
class SegmentTree:

    def __init__(self, data):
        self.data = data[:]
        self.n = len(data)
        self.tree = [0] * (self.n * 4)
        self._build(0, self.n - 1, 1)

    def _build(self, start, end, idx):
        if start == end:
            self.tree[idx] = self.data[start]
            return
        mid = (start + end) // 2
        self._build(start, mid, 2 * idx)
        self._build(mid + 1, end, 2 * idx + 1)
        self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, left, right):
        return self._query(0, self.n - 1, left, right, 1)

    def _query(self, start, end, l, r, idx):
        if l <= start and end <= r:
            return self.tree[idx]
        mid = (start + end) // 2
        left, right = -math.inf, -math.inf
        if l <= mid:
            left = self._query(start, mid, l, r, 2 * idx)
        if r > mid:
            right = self._query(mid + 1, end, l, r, 2 * idx + 1)
        return max(left, right)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tree = SegmentTree(nums)

        n = len(nums)
        res = []
        for i in range(k - 1, n):
            l, r = i - k + 1, i
            max0 = tree.query(l, r)
            res.append(max0)

        return res


# deque & pop smaller num than new num
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # store index, the biggest num on the dq[0]
        res = []

        for i, num in enumerate(nums):
            # pop the elements which are smaller than num
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # biggest num is not in the range
            if dq[0] == i - k:
                dq.popleft()

            if i - k + 1 >= 0:
                res.append(nums[dq[0]])

        return res
