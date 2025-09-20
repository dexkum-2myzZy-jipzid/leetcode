class Solution {
    public int maxProfit(int[] prices) {
        // dp[i][0] sell
        // dp[i][1] buy/hold
        int n = prices.length;
        int[][] dp = new int[n][2];

        // init dp
        dp[0][0] = 0;
        dp[0][1] = -prices[0];

        // iterate
        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], -prices[i]);
        }

        // for (int[] x : dp) {
        // System.out.print("\t" + x[0]);
        // }
        // System.out.println();
        // for (int[] x : dp) {
        // System.out.print("\t" + x[1]);
        // }

        return dp[n - 1][0];
    }
}