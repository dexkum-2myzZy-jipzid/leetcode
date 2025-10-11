class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        // bfs, only two directions
        // horizontal, vertically
        let dirs = [(0, 1), (1, 0)]

        var board = board
        let m = board.count, n = board[0].count
        var res = 0

        for i in 0 ..< m {
            for j in 0 ..< n {
                // if cur is X, check horizontally and vertically
                if board[i][j] == "X" {
                    res += 1
                    var x = 1
                    while i + x < m && board[i + x][j] == "X" {
                        board[i + x][j] = "."
                        x += 1
                    }
                    x = 1
                    while j + x < n && board[i][j + x] == "X" {
                        board[i][j + x] = "."
                        x += 1
                    }
                }
            }
        }

        return res
    }
}

// optimized version
class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        // bfs, only two directions
        // horizontal, vertically
        let dirs = [(0, 1), (1, 0)]

        var board = board
        let m = board.count, n = board[0].count
        var res = 0

        for i in 0 ..< m {
            for j in 0 ..< n {
                // if cur is X, check horizontally and vertically
                if board[i][j] != "X" { continue }

                // check left
                if i - 1 >= 0 && board[i - 1][j] == "X" { continue }
                // check top
                if j - 1 >= 0 && board[i][j - 1] == "X" { continue }

                res += 1
            }
        }

        return res
    }
}
