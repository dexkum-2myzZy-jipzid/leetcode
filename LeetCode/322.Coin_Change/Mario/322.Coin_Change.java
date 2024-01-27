class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 0;

        for (int i = 1; i < dp.length; i++) {
            int res = -1;
            for (int c : coins) {
                if (i >= c && dp[i - c] != -1) {
                    if (res == -1) {
                        res = dp[i - c] + 1;
                    } else {
                        res = Math.min(res, dp[i - c] + 1);
                    }
                }
            }
            dp[i] = res;
        }
        return dp[dp.length - 1];
    }
}