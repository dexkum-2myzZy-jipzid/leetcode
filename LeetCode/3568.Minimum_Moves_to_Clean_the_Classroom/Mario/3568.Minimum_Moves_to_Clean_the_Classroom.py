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
