class Solution {
    public int maxProfit(int k, int[] prices) {
        // dp[i][0][k] kth time buy/hold stock on ith day
        // dp[i][1][k] kth time sell stock on ith day
        int n = prices.length;
        int[][][] dp = new int[n][2][k];

        // init dp
        for (int i = 0; i < k; i++) {
            dp[0][0][i] = -prices[0];
            dp[0][1][i] = 0;
        }

        for (int i = 1; i < n; i++) {
            dp[i][0][0] = Math.max(dp[i - 1][0][0], -prices[i]);
            dp[i][1][0] = Math.max(dp[i - 1][1][0], dp[i - 1][0][0] + prices[i]);
            for (int j = 1; j < k; j++) {
                dp[i][0][j] = Math.max(dp[i - 1][0][j], dp[i - 1][1][j - 1] - prices[i]);
                dp[i][1][j] = Math.max(dp[i - 1][1][j], dp[i - 1][0][j] + prices[i]);
            }
        }

        return dp[n - 1][1][k - 1];
    }
}