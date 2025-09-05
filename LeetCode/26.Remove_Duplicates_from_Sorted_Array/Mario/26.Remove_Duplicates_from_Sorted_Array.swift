class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        // two pointers
        // i: tracks the position for unique elment
        // j: traverses entire nums
        let n = nums.count
        var i = 0
        for j in 1 ..< n {
            if nums[j] != nums[i] {
                i += 1
                nums[i] = nums[j]
            }
        }
        return i + 1
    }
}
