struct Point: Comparable {
    let t: Int, x: Int, y: Int

    static func < (_ lhs: Point, _ rhs: Point) -> Bool {
        lhs.t < rhs.t
    }
}

class Solution {
    func swimInWater(_ grid: [[Int]]) -> Int {
        // (0,0) -> (n-1, n-1)
        let n = grid.count
        guard n > 1 else { return grid[0][0] }

        var heap = Heap<Point>()
        heap.insert(Point(t: grid[0][0], x: 0, y: 0))
        var seen = Set<Int>() // hold grid[i][j]

        let dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while !heap.isEmpty {
            guard let p = heap.popMin() else { break }

            if p.x == n - 1 && p.y == n - 1 {
                return p.t
            }

            for (dx, dy) in dirs {
                let nx = dx + p.x, ny = dy + p.y
                if nx >= 0 && nx < n && ny >= 0 && ny < n && !seen.contains(grid[nx][ny]) {
                    let nt = grid[nx][ny]
                    seen.insert(nt)
                    heap.insert(Point(t: max(nt, p.t), x: nx, y: ny))
                }
            }
        }

        return -1
    }
}
