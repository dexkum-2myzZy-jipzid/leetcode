class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)

        var left = 0
        for (i, num) in nums.enumerated() {
            let right = total - num - left
            if left == right {
                return i
            }
            left += num
        }

        return -1
    }
}
