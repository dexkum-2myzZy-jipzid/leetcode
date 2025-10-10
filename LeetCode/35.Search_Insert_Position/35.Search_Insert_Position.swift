class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var l = 0, r = n
        while l < r {
            let m = (l + r) >> 1
            if nums[m] < target {
                l = m + 1
            } else {
                r = m
            }
        }

        return l
    }
}
