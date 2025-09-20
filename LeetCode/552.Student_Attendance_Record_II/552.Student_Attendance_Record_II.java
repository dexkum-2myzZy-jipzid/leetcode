class Solution {
    public int checkRecord(int n) {
        final int MOD = 1000000007;
        // dp
        long[][][] dp = new long[n][2][3];

        // init dp
        // i: ith day, j: Absent day, k: consecutive days
        dp[0][0][0] = 1;
        dp[0][1][0] = 1;
        dp[0][0][1] = 1;

        for (int i = 1; i < n; i++) {
            // 0 A && 0 L
            dp[i][0][0] = dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2];

            // 1 A && 0 L
            dp[i][1][0] = dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2] + dp[i - 1][0][0] + dp[i - 1][0][1]
                    + dp[i - 1][0][2];

            // 0A && 1L
            dp[i][0][1] = dp[i - 1][0][0];

            // 0A && 2L
            dp[i][0][2] = dp[i - 1][0][1];

            // 1A && 1L
            dp[i][1][1] = dp[i - 1][1][0];

            // 1A && 2L
            dp[i][1][2] = dp[i - 1][1][1];

            for (int j = 0; j <= 1; j++) {
                for (int k = 0; k <= 2; k++) {
                    dp[i][j][k] %= MOD;
                }
            }
        }

        long sum = 0;
        for (int j = 0; j <= 1; j++) {
            for (int k = 0; k <= 2; k++) {
                sum = (sum + dp[n - 1][j][k]) % MOD;
            }
        }

        return (int) sum;
    }
}