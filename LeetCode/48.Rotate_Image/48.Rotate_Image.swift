class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        guard n > 1 else { return }

        // i: 0 ..< ceil(n/2),  j: 0 ..< floor(n/2)
        for i in 0 ..< ((n + 1) / 2) {
            for j in 0 ..< (n / 2) {
                // (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i)
                let cur = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = cur
            }
        }
    }
}

class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        guard n > 1 else { return }

        // i: 0 ..< ceil(n/2),  j: 0 ..< floor(n/2)
        for i in 0 ..< ((n + 1) / 2) {
            for j in 0 ..< (n / 2) {
                // (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i)
                (matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i]) = (matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j])
            }
        }
    }
}
