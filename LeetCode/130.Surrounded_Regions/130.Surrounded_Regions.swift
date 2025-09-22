class Solution {
    func solve(_ board: inout [[Character]]) {
        // surround means no "0" connect edges
        // 1. check 4 sides about this board, if has '0', I will do dfs,
        // mark (i, j), put it into set
        // 2. iterate all elements, if it is '0' and not in set, so replace it with 'X'

        let m = board.count, n = board[0].count

        let O: Character = "O", X: Character = "X", S: Character = "S"

        func bfs(_ point: (Int, Int)) {
            let dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            var q = [point]
            board[point.0][point.1] = S
            var head = 0

            while head < q.count {
                let (i, j) = q[head]
                head += 1

                for (di, dj) in dirs {
                    let ni = i + di, nj = j + dj
                    if ni >= 0, ni < m, nj >= 0, nj < n, board[ni][nj] == O {
                        q.append((ni, nj))
                        board[ni][nj] = S
                    }
                }
            }
        }

        // horizontal sides
        for i in 0 ..< n {
            if board[0][i] == O {
                bfs((0, i))
            }
            if board[m - 1][i] == O {
                bfs((m - 1, i))
            }
        }

        // vertical sides
        for i in 0 ..< m {
            if board[i][0] == O {
                bfs((i, 0))
            }
            if board[i][n - 1] == O {
                bfs((i, n - 1))
            }
        }

        for i in 0 ..< m {
            for j in 0 ..< n {
                if board[i][j] == O {
                    board[i][j] = X
                } else if board[i][j] == S {
                    board[i][j] = O
                }
            }
        }
    }
}
