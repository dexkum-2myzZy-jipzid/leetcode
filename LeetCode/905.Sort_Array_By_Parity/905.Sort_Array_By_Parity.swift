class Solution {
    func sortArrayByParity(_ nums: [Int]) -> [Int] {
        // two pointers,
        // i: traverse entire nums
        // j: only shift when num is even

        var nums = nums
        let n = nums.count
        var j = 0

        for (i, num) in nums.enumerated() {
            if num % 2 == 0 {
                nums.swapAt(i, j)
                j += 1
            }
        }

        return nums
    }
}
