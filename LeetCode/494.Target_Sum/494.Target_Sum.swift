class Solution {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        // sum(P) - sum(N) = target
        // sum(p) + sum(N) = sum(nums)
        // 2*sum(p) = target + sum(nums)

        let total = nums.reduce(0, +)
        if (total + target) % 2 == 1 { return 0 }
        let pTotal = (total + target) / 2

        if pTotal < 0 { return 0 }

        // how many way to add num to be pTotal
        let n = nums.count

        var dp = Array(repeating: 0, count: pTotal + 1)
        dp[0] = 1

        for num in nums {
            for j in stride(from: pTotal, through: num, by: -1) {
                dp[j] += dp[j - num]
            }
        }

        return dp[pTotal]
    }
}
