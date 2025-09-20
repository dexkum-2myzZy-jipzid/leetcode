class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int n = nums.length;
        long[][] dp = new long[n + 1][2];

        // init
        dp[0][0] = 0;
        dp[0][1] = Integer.MIN_VALUE;

        for (int i = 1; i < n + 1; i++) {
            dp[i][0] = Math.max(dp[i - 1][0] + nums[i - 1], dp[i - 1][1] + (nums[i - 1] ^ k));
            dp[i][1] = Math.max(dp[i - 1][1] + nums[i - 1], dp[i - 1][0] + (nums[i - 1] ^ k));
        }

        return dp[n][0];
    }
}