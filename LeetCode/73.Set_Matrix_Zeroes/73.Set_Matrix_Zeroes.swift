class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        let m = matrix.count, n = matrix[0].count
        var firstRowZero = false, firstColZero = false

        // check first row is all zero or not
        for i in 0 ..< n {
            if matrix[0][i] == 0 {
                firstRowZero = true
                break
            }
        }

        // check first col is all zero or not
        for i in 0 ..< m {
            if matrix[i][0] == 0 {
                firstColZero = true
                break
            }
        }

        // mark which row and clos will be set to zero in first col and row
        for i in 1 ..< m {
            for j in 1 ..< n {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }

        // if matrix[i][0] == 0, set cur row is all 0
        for i in 1 ..< m {
            if matrix[i][0] == 0 {
                for j in 0 ..< n {
                    matrix[i][j] = 0
                }
            }
        }

        // if matrix[0][i] == 0, set cur col is all 0
        for i in 1 ..< n {
            if matrix[0][i] == 0 {
                for j in 0 ..< m {
                    matrix[j][i] = 0
                }
            }
        }

        if firstRowZero {
            for i in 0 ..< n {
                matrix[0][i] = 0
            }
        }

        if firstColZero {
            for i in 0 ..< m {
                matrix[i][0] = 0
            }
        }
    }
}
