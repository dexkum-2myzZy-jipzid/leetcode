class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;

        int buy1 = -prices[0];
        int sell1 = 0;
        int buy2 = -prices[0];
        int sell2 = 0;

        for (int i = 1; i < n; i++) {
            buy1 = Math.max(buy1, 0 - prices[i]);
            sell1 = Math.max(sell1, buy1 + prices[i]);
            buy2 = Math.max(buy2, sell1 - prices[i]);
            sell2 = Math.max(sell2, buy2 + prices[i]);
        }

        return sell2;
    }
}

// Easy to understand version
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][5];

        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        dp[0][2] = 0;
        dp[0][3] = -prices[0];
        dp[0][4] = 0;

        for (int i = 1; i < n; i++) {
            dp[i][0] = dp[i - 1][0];
            dp[i][1] = Math.max(dp[i - 1][1], dp[i][0] - prices[i]);
            dp[i][2] = Math.max(dp[i - 1][2], dp[i - 1][1] + prices[i]);
            dp[i][3] = Math.max(dp[i - 1][3], dp[i - 1][2] - prices[i]);
            dp[i][4] = Math.max(dp[i - 1][4], dp[i - 1][3] + prices[i]);
        }

        return dp[n - 1][4];
    }
}

// 08/02/2024
class Solution {
    public int maxProfit(int[] prices) {
        // dp[i][0][0] first time sell stock
        // dp[i][1][0] first time buy/hold stock
        // dp[i][0][1] second time sell stock
        // dp[i][1][1] second time buy/hold stock

        int n = prices.length;
        int[][][] dp = new int[n][2][2];

        dp[0][0][0] = 0;
        dp[0][1][0] = -prices[0];
        dp[0][0][1] = 0;
        dp[0][1][1] = -prices[0];

        for (int i = 1; i < n; i++) {
            dp[i][0][0] = Math.max(dp[i - 1][0][0], dp[i - 1][1][0] + prices[i]);
            dp[i][1][0] = Math.max(dp[i - 1][1][0], -prices[i]);
            dp[i][1][1] = Math.max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i]);
            dp[i][0][1] = Math.max(dp[i - 1][0][1], dp[i - 1][1][1] + prices[i]);
        }

        return dp[n - 1][0][1];
    }
}