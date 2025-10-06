class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var res: [[Int]] = []

        while res.count < numRows {
            if res.isEmpty {
                res.append([1])
            } else if let top = res.last {
                var next = [1]
                if top.count >= 2 {
                    for i in 1 ..< top.count {
                        next.append(top[i] + top[i - 1])
                    }
                }
                next.append(1)
                res.append(next)
            }
        }

        return res
    }
}
