class Solution {
    public int change(int amount, int[] coins) {
        int m = coins.length;
        int[] dp = new int[amount + 1];

        for (int i = 0; i <= amount; i += coins[0]) {
            dp[i] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = coins[i]; j <= amount; j++) {
                dp[j] = dp[j] + dp[j - coins[i]];
            }
            // System.out.println(Arrays.toString(dp));
        }

        return dp[amount];
    }
}