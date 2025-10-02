class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        var dp = Array(repeating: amount + 1, count: amount + 1)

        // init dp
        dp[0] = 0

        for coin in coins {
            if amount < coin { continue }
            for i in coin ... amount {
                dp[i] = min(dp[i - coin] + 1, dp[i])
            }
        }

        return dp[amount] == amount + 1 ? -1 : dp[amount]
    }
}
