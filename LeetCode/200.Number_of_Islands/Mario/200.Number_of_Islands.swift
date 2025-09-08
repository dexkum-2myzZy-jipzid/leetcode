class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        var grid = grid
        let m = grid.count
        guard m > 0 else { return 0 }
        let n = grid[0].count
        let dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        var q: Deque<(Int, Int)> = []

        var res = 0
        for i in 0 ..< m {
            for j in 0 ..< n {
                if grid[i][j] == "1" {
                    res += 1
                    grid[i][j] == "0"
                    q.append((i, j))
                    while let (x, y) = q.popFirst() {
                        for (dx, dy) in dirs {
                            let nx = dx + x, ny = dy + y
                            if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == "1" {
                                q.append((nx, ny))
                                grid[nx][ny] = "0"
                            }
                        }
                    }
                }
            }
        }

        return res
    }
}
