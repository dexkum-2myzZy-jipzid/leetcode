class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        let n = nums.count
        var nums = nums
        var res: [[Int]] = []

        func backtrack(_ i: Int) {
            if i == nums.count {
                res.append(nums)
                return
            }

            for j in i ..< n {
                nums.swapAt(j, i)
                backtrack(i + 1)
                nums.swapAt(i, j)
            }
        }

        backtrack(0)

        return res
    }
}
