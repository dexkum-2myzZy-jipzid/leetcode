class Solution {
    func kthSmallest(_ matrix: [[Int]], _ k: Int) -> Int {
        let n = matrix.count

        func countSmall(_ x: Int) -> Int {
            var cnt = 0
            for row in matrix {
                var l = 0, r = n
                while l < r {
                    let m = (l + r) >> 1
                    if row[m] <= x {
                        l = m + 1
                    } else {
                        r = m
                    }
                }
                cnt += l
            }
            return cnt
        }

        var l = matrix[0][0], r = matrix[n - 1][n - 1]
        while l < r {
            let m = (l + r) >> 1
            if countSmall(m) < k {
                l = m + 1
            } else {
                r = m
            }
        }

        return l
    }
}
