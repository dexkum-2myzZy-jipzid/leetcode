class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let m = matrix.count, n = matrix[0].count

        var dic: [Int: Int] = [:]

        for i in 0 ..< m {
            for j in 0 ..< n {
                let key = i - j
                if let val = dic[key] {
                    if val != matrix[i][j] {
                        return false
                    }
                } else {
                    dic[key] = matrix[i][j]
                }
            }
        }

        return true
    }
}

class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let m = matrix.count, n = matrix[0].count

        for i in 1 ..< m {
            for j in 1 ..< n {
                if matrix[i][j] != matrix[i - 1][j - 1] {
                    return false
                }
            }
        }

        return true
    }
}
