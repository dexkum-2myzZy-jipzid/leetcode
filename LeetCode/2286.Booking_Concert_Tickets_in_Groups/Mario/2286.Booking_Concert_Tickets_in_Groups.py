#!/usr/bin/env python3


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.data = [m] * n
        self.sumTree = [0] * (4 * n)
        self.maxTree = [0] * (4 * n)
        self._build(0, n - 1, 1)

    def gather(self, k: int, maxRow: int) -> List[int]:
        # query first fill k seats row in [0, maxRow]
        res = self._findFirst(0, self.n - 1, 0, maxRow, 1, k)
        if res == -1:
            return []
        else:
            # update row
            c = self.m - self.data[res]
            val = self.data[res] - k
            self._update(0, self.n - 1, res, val, 1)
            return [res, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        # query sum
        res = self._query(0, self.n - 1, 0, maxRow, 1)
        if res < k:
            return False
        else:
            row = self._findFirst(0, self.n - 1, 0, maxRow, 1, 1)
            while k:
                seats = self.data[row]
                if seats >= k:
                    self._update(0, self.n - 1, row, seats - k, 1)
                    k = 0
                else:
                    self._update(0, self.n - 1, row, 0, 1)
                    k -= seats
                    row += 1
        return True

    def _build(self, l, r, i):
        if l == r:
            self.sumTree[i] = self.data[l]
            self.maxTree[i] = self.data[l]
            return
        m = (l + r) // 2
        self._build(l, m, 2 * i)
        self._build(m + 1, r, 2 * i + 1)
        self.sumTree[i] = self.sumTree[2 * i] + self.sumTree[2 * i + 1]
        self.maxTree[i] = max(self.maxTree[2 * i], self.maxTree[2 * i + 1])

    def _query(self, l, r, L, R, i):
        if L <= l and r <= R:
            return self.sumTree[i]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res += self._query(l, m, L, R, 2 * i)
        if m < R:
            res += self._query(m + 1, r, L, R, 2 * i + 1)
        return res

    def _update(self, l, r, p, v, i):
        if l == r:
            self.sumTree[i] = v
            self.data[p] = v
            self.maxTree[i] = v
            return
        m = (l + r) // 2
        if p <= m:
            self._update(l, m, p, v, 2 * i)
        else:
            self._update(m + 1, r, p, v, 2 * i + 1)
        self.sumTree[i] = self.sumTree[2 * i] + self.sumTree[2 * i + 1]
        self.maxTree[i] = max(self.maxTree[2 * i], self.maxTree[2 * i + 1])

    def _findFirst(self, l, r, L, R, i, k):
        if r < L or l > R:
            return -1
        if L <= l and r <= R:
            if self.maxTree[i] < k:
                return -1
            if l == r:
                return l
        m = (l + r) // 2
        left = self._findFirst(l, m, L, R, 2 * i, k)
        if left != -1:
            return left
        else:
            return self._findFirst(m + 1, r, L, R, 2 * i + 1, k)


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
