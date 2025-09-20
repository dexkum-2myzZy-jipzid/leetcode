class Solution {
    func findDiagonalOrder(_ mat: [[Int]]) -> [Int] {
        // key = i + j
        let m = mat.count, n = mat[0].count
        var diag = Array(repeating: [Int](), count: m + n - 1)
        for i in 0 ..< m {
            for j in 0 ..< n {
                diag[i + j].append(mat[i][j])
            }
        }

        var res: [Int] = []
        for (i, lst) in diag.enumerated() {
            if i & 1 == 1 {
                res.append(contentsOf: lst)
            } else {
                res.append(contentsOf: Array(lst.reversed()))
            }
        }
        return res
    }
}
