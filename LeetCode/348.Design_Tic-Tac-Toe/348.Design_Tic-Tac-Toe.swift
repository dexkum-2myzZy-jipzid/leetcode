class TicTacToe {
    // rows, if play 1, rows[row] += 1, play2, -1
    var rows: [Int], cols: [Int], diag: [Int]
    let n: Int

    init(_ n: Int) {
        self.n = n
        rows = Array(repeating: 0, count: n)
        cols = Array(repeating: 0, count: n)
        diag = [0, 0] // diag, antidiag
    }

    func move(_ row: Int, _ col: Int, _ player: Int) -> Int {
        var add = player == 1 ? 1 : -1
        rows[row] += add
        cols[col] += add
        if row == col { diag[0] += add }
        if row + col == n - 1 { diag[1] += add }

        if abs(rows[row]) == n || abs(cols[col]) == n || abs(diag[0]) == n || abs(diag[1]) == n { return player }
        return 0
    }
}
