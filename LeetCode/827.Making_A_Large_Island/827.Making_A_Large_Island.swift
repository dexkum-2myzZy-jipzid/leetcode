// UnionFind
class UnionFind {
    var parent: [Int]
    var size: [Int]

    init(_ n: Int) {
        parent = Array(0 ..< n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ x: Int, _ y: Int) {
        var rx = find(x), ry = find(y)
        guard rx != ry else { return }

        if ry > rx {
            (rx, ry) = (ry, rx)
        }
        parent[ry] = rx
        size[rx] += size[ry]
    }

    func connected(_ x: Int, _ y: Int) -> Bool {
        return find(x) == find(y)
    }
}

struct Point: Hashable {
    let x: Int, y: Int
}

class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        // union find
        let n = grid.count

        func toIdx(_ i: Int, _ j: Int) -> Int {
            i * n + j
        }

        var zeros = Set<Point>()
        let uf = UnionFind(n * n)

        for i in 0 ..< n {
            for j in 0 ..< n {
                if grid[i][j] == 0 {
                    zeros.insert(Point(x: i, y: j))
                    continue
                }

                // grid[i][j] == 1
                for (di, dj) in [(0, 1), (1, 0)] {
                    let ni = di + i, nj = dj + j
                    if ni >= 0 && ni < n && nj >= 0 && nj < n && grid[ni][nj] == 1 {
                        uf.union(toIdx(i, j), toIdx(ni, nj))
                    }
                }
            }
        }

        let dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        var res = 0
        for p in zeros {
            var size = 1
            var seen = Set<Int>()
            for (dx, dy) in dirs {
                let nx = p.x + dx, ny = p.y + dy
                if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == 1 {
                    let idx = toIdx(nx, ny)
                    let parent = uf.find(idx)
                    if !seen.contains(parent) {
                        seen.insert(parent)
                        size += uf.size[parent]
                    }
                }
            }
            res = max(res, size)
        }

        return max(res, uf.size.max() ?? 0)
    }
}

// DFS
class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        var grid = grid // 需要可变
        let n = grid.count
        guard n > 0 else { return 0 }

        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var id = 2 // 岛屿标号从 2 开始（避开 0/1）
        var area: [Int: Int] = [:] // id -> 岛屿面积
        var maxArea = 0
        var hasZero = false

        // 迭代 DFS 染色，返回该岛屿的面积
        func colorAndCount(_ sr: Int, _ sc: Int, _ id: Int) -> Int {
            var stack: [(Int, Int)] = [(sr, sc)]
            grid[sr][sc] = id
            var size = 0

            while let (r, c) = stack.popLast() {
                size += 1
                for (dr, dc) in dirs {
                    let nr = r + dr, nc = c + dc
                    if nr >= 0, nr < n, nc >= 0, nc < n, grid[nr][nc] == 1 {
                        grid[nr][nc] = id
                        stack.append((nr, nc))
                    }
                }
            }
            return size
        }

        // 1) 染色并统计每个岛的面积
        for r in 0 ..< n {
            for c in 0 ..< n {
                if grid[r][c] == 1 {
                    let size = colorAndCount(r, c, id)
                    area[id] = size
                    maxArea = max(maxArea, size)
                    id += 1
                } else if grid[r][c] == 0 {
                    hasZero = true
                }
            }
        }

        // 如果已经没有 0，可以直接返回整图面积
        if !hasZero { return maxArea } // 等同于 n * n

        // 2) 枚举每个 0，尝试翻转并连接相邻不同岛屿
        for r in 0 ..< n {
            for c in 0 ..< n {
                if grid[r][c] == 0 {
                    var seen: Set<Int> = []
                    var sum = 1 // 翻转当前 0 带来的 +1

                    for (dr, dc) in dirs {
                        let nr = r + dr, nc = c + dc
                        if nr >= 0, nr < n, nc >= 0, nc < n {
                            let nid = grid[nr][nc]
                            if nid > 1, !seen.contains(nid) {
                                seen.insert(nid)
                                sum += area[nid] ?? 0
                            }
                        }
                    }

                    maxArea = max(maxArea, sum)
                    if maxArea == n * n { return maxArea } // 早停
                }
            }
        }

        return maxArea
    }
}
