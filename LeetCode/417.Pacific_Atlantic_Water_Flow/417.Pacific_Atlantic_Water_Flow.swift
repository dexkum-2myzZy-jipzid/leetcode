class Solution {
    func pacificAtlantic(_ heights: [[Int]]) -> [[Int]] {
        // result[i] can flow to both P & A
        // 0:unvisited, 1: P, 2: A, 3:Both: 4:None

        let m = heights.count, n = heights[0].count

        // can visited
        var pac = Array(repeating: Array(repeating: false, count: n), count: m)
        var alt = Array(repeating: Array(repeating: false, count: n), count: m)

        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        func bfs(_ src: (Int, Int), _ seen: inout [[Bool]]) {
            if seen[src.0][src.1] { return }

            var q = [src]
            var head = 0

            while head < q.count {
                let (x, y) = q[head]
                head += 1

                seen[x][y] = true

                for (dx, dy) in dirs {
                    let nx = dx + x, ny = dy + y
                    if nx >= 0, nx < m, ny >= 0, ny < n, !seen[nx][ny], heights[nx][ny] >= heights[x][y] {
                        seen[nx][ny] = true
                        q.append((nx, ny))
                    }
                }
            }
        }

        // Pacific, 1st row & col
        for i in 0 ..< n {
            bfs((0, i), &pac)
        }
        for j in 1 ..< m {
            bfs((j, 0), &pac)
        }

        // Atlantic, last row & col
        for i in 0 ..< n {
            bfs((m - 1, i), &alt)
        }
        for j in 0 ..< m {
            bfs((j, n - 1), &alt)
        }

        var res: [[Int]] = []
        for i in 0 ..< m {
            for j in 0 ..< n {
                if pac[i][j], alt[i][j] { res.append([i, j]) }
            }
        }

        return res
    }
}
