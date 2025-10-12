class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        let n = nums.count
        guard n > 1 else { return true }

        var reach = 0
        for i in 0 ..< n {
            if i > reach { return false }
            reach = max(reach, i + nums[i])
        }

        return true
    }
}
