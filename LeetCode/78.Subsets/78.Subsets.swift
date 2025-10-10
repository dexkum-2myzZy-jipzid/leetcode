class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        let n = nums.count
        var res: [[Int]] = []

        func dfs(_ i: Int, _ path: [Int]) {
            guard i <= n else { return }
            res.append(path)

            for j in i ..< n {
                dfs(j + 1, path + [nums[j]])
            }
        }

        dfs(0, [])

        return res
    }
}
