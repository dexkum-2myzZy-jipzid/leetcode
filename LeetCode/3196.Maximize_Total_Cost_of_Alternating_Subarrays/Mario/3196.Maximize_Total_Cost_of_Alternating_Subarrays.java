class Solution {
    public long maximumTotalCost(int[] nums) {
        int n = nums.length;
        // dp[n][2]
        // dp[0][0] dp[0][1] = nums[0]
        // *(-1) dp[i][0] = dp[i-1][1] + (-1) * nums[i]
        // *(1) dp[i][1] = Math.max(dp[i-1][0], dp[i-1][1]) + (1)*nums[i]

        long[][] dp = new long[n][2];
        dp[0][0] = nums[0];
        dp[0][1] = nums[0];

        for (int i = 1; i < n; i++) {
            dp[i][0] = dp[i - 1][1] + (-1) * nums[i];
            dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][1]) + nums[i];
        }

        return Math.max(dp[n - 1][0], dp[n - 1][1]);
    }
}