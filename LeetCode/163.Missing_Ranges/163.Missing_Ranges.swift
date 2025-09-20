class Solution {
    func findMissingRanges(_ nums: [Int], _ lower: Int, _ upper: Int) -> [[Int]] {
        let nums = [lower - 1] + nums + [upper + 1]
        let n = nums.count

        var res: [[Int]] = []

        for i in 1 ..< n {
            if nums[i - 1] + 1 < nums[i] {
                res.append([nums[i - 1] + 1, nums[i] - 1])
            }
        }

        return res
    }
}
