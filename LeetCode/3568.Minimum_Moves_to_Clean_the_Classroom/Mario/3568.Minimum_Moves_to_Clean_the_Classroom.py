#!/usr/bin/env python3


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # brute force again? BFS
        m, n = len(classroom), len(classroom[0])
        total = 0
        start = []
        litter_idx = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = [i, j]
                elif classroom[i][j] == "L":
                    litter_idx[(i, j)] = idx
                    total += 1
                    idx += 1
        # print(total)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        visited = dict()
        queue.append((start[0], start[1], energy, 0, 0))  # i, j, energy, mask, step
        visited[(start[0], start[1], 0)] = energy

        while queue:
            x, y, en, mask, step = queue.popleft()
            if mask == (1 << total) - 1:
                return step
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                    nen = en - 1
                    if nen < 0:
                        if classroom[nx][ny] != "R":
                            continue
                    elif classroom[nx][ny] == "R":
                        nen = energy
                    nmask = mask
                    if classroom[nx][ny] == "L":
                        nmask |= 1 << litter_idx[(nx, ny)]
                    key = (nx, ny, nmask)
                    if nen < 0:
                        continue
                    # 只在能量更大时扩展同一状态
                    if key not in visited or nen > visited[key]:
                        visited[key] = nen
                        queue.append((nx, ny, nen, nmask, step + 1))
        return -1


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        # state:(row, column, mask, energy)
        # visited[row][col][mask][energy]
        litter_dic = {}  # (i, j): int
        litter_cnt = sx = sy = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "L":
                    litter_dic[(i, j)] = litter_cnt
                    litter_cnt += 1
                elif classroom[i][j] == "S":
                    sx, sy = i, j

        # handle edge case
        if litter_cnt == 0:
            return 0

        full_mask = (1 << litter_cnt) - 1
        visited = [[[-1] * (full_mask + 1) for _ in range(n)] for _ in range(m)]

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque([(sx, sy, full_mask, energy)])
        visited[sx][sy][full_mask] = energy
        step = 0

        while q:
            size = len(q)
            for _ in range(size):
                i, j, mask, e = q.popleft()

                # collect all litters
                if mask == 0:
                    return step
                # no energy
                if e == 0:
                    continue

                for di, dj in DIRS:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and classroom[ni][nj] != "X":
                        cur = classroom[ni][nj]
                        # reset engery
                        new_e = energy if cur == "R" else e - 1
                        # update mask
                        new_m = (
                            mask & ~(1 << litter_dic[(ni, nj)]) if cur == "L" else mask
                        )
                        # update visited
                        if new_e > visited[ni][nj][new_m]:
                            visited[ni][nj][new_m] = new_e
                            q.append((ni, nj, new_m, new_e))

            step += 1

        return -1
