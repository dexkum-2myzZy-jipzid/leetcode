class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        let n = nums.count
        var l = 0, r = n - 1

        while l < r {
            let mid = (l + r) >> 1
            if nums[mid] < nums[mid + 1] {
                l = mid + 1
            } else {
                r = mid
            }
        }

        return l
    }
}
