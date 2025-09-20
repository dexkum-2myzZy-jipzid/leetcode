class Solution {
    public int maximumSumSubsequence(int[] nums, int[][] queries) {
        int n = nums.length;
        int[][] dp = new int[n + 1][2];

        for (int i = 1; i <= n; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = Math.max(dp[i - 1][0] + nums[i - 1], dp[i - 1][1]);
        }

        long result = 0;
        for (int[] query : queries) {
            int index = query[0], val = query[1];
            nums[index] = val;
            for (int i = index + 1; i <= n; i++) {
                dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
                dp[i][1] = Math.max(dp[i - 1][0] + nums[i - 1], dp[i - 1][1]);
            }
            result = (result + Math.max(dp[n][0], dp[n][1])) % 1000_000_007;
        }

        return (int) result;
    }
}