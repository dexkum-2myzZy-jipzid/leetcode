#!/usr/bin/env python3


# bfs
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # bfs
        # (i,j) -> (i+1, j) if i == 0, (i, j+1)

        m, n = len(mat), len(mat[0])
        q = deque([])
        q.append((0, 0))

        res = []
        even = False
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                i, j = q.popleft()
                tmp.append(mat[i][j])
                if i + 1 < m:
                    q.append((i + 1, j))
                if i == 0 and j + 1 < n:
                    q.append((i, j + 1))
            if even:
                tmp.reverse()
            res += tmp
            even = not even

        return res


# simulate the whole process
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        k = (m - 1) + (n - 1)

        res = []
        for d in range(k + 1):
            even = (d + 1) % 2 == 0

            # start point
            row = 0 if d < n else d - (n - 1)
            col = d if d < n else n - 1

            # one pass
            tmp = []
            while row < m and col >= 0:
                tmp.append(mat[row][col])
                row += 1
                col -= 1

            if not even:
                tmp.reverse()

            res += tmp

        return res
