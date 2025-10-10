class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        // each element can be used once
        // minimized max pair sum
        let nums = nums.sorted()
        let n = nums.count

        var res = 0
        var l = 0, r = n - 1
        while l < r {
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        }

        return res
    }
}
