class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        // dp[i][0] / dp[i][1] represent max profit hold / sell stock
        // dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]) // still hold prev stock or buy current stock
        // dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        let n = prices.count
        var dp = Array(repeating: [0, 0], count: n)

        // init dp
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in 1 ..< n {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        }

        return dp[n - 1].max()!
    }
}

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        let n = prices.count

        var hold = -prices[0], sell = 0

        for i in 1 ..< n {
            let prevHold = hold
            hold = max(hold, sell - prices[i])
            sell = max(sell, prevHold + prices[i])
        }

        return max(hold, sell)
    }
}
