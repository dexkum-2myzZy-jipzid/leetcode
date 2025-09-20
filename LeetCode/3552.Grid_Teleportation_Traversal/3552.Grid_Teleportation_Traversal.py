#!/usr/bin/env python3


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])

        dic = defaultdict(list)  # "A":[(i, j)]
        for i, s in enumerate(matrix):
            for j, c in enumerate(s):
                if c.isupper():
                    dic[c].append((i, j))

        DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()

            d = dis[x][y]

            if x == m - 1 and y == n - 1:
                return d

            c = matrix[x][y]
            if c in dic:
                for i, j in dic[c]:
                    if d < dis[i][j]:
                        dis[i][j] = d
                        q.appendleft((i, j))
                del dic[c]

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and matrix[nx][ny] != "#"
                    and d + 1 < dis[nx][ny]
                ):
                    q.append((nx, ny))
                    dis[nx][ny] = d + 1

        return -1
