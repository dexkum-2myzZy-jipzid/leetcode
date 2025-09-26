class Solution {
    func rob(_ nums: [Int]) -> Int {
        // dp[i] represent max amount you rob in the nums[:i]
        // dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        let n = nums.count
        guard n >= 2 else { return nums[0] }

        var dp: [Int] = Array(repeating: 0, count: n + 1)

        dp[1] = nums[0]

        for i in 2 ... n {
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        }

        return dp[n]
    }
}
