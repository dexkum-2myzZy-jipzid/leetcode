class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var write = 0

        for (i, num) in nums.enumerated() {
            if num != val {
                nums[write] = num
                write += 1
            }
        }
        return write
    }
}
