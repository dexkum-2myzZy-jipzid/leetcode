class Solution {
    func shortestPathBinaryMatrix(_ grid: [[Int]]) -> Int {
        let n = grid.count
        guard n > 0 else { return -1 }

        if grid[0][0] == 1 || grid[n - 1][n - 1] == 1 { return -1 }

        let dirs = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)]

        var queue: [(Int, Int, Int)] = []
        var head = 0

        queue.append((0, 0, 1))
        var g = grid
        g[0][0] = 1

        while head < queue.count {
            let (i, j, dis) = queue[head]
            head += 1

            if i == n - 1 && j == n - 1 {
                return dis
            }

            for (di, dj) in dirs {
                let ni = i + di, nj = j + dj

                // invalid case
                if ni < 0 || ni >= n || nj < 0 || nj >= n || g[ni][nj] == 1 {
                    continue
                }

                g[ni][nj] = 1
                queue.append((ni, nj, dis + 1))
            }
        }

        return -1
    }
}
