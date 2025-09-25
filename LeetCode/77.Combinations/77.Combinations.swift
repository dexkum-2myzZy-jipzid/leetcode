class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        let nums = Array(1 ... n)

        var res: [[Int]] = []
        func backtrack(_ i: Int, _ path: [Int]) {
            if path.count == k {
                res.append(path)
                return
            }

            for j in i ..< n {
                backtrack(j + 1, path + [nums[j]])
            }
        }

        backtrack(0, [])

        return res
    }
}
