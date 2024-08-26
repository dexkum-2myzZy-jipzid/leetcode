class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][2];

        // dp[i][0] maxProductWith ith element
        // dp[i][1] minProductwith ith element
        dp[0][0] = nums[0];
        dp[0][1] = nums[0];

        int result = dp[0][0];
        for (int i = 1; i < n; i++) {
            int cur = nums[i];
            // update dp
            if (cur != 0) {
                dp[i][0] = Math.max(cur, Math.max(dp[i - 1][0] * cur, dp[i - 1][1] * cur));
                dp[i][1] = Math.min(cur, Math.min(dp[i - 1][0] * cur, dp[i - 1][1] * cur));
            }

            // store max result
            result = Math.max(dp[i][0], result);
        }

        return result;
    }
}