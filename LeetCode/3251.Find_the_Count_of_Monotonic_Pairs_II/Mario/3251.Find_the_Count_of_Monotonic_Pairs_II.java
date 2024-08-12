class Solution {

    public int countOfPairs(int[] nums) {
        int MOD = 1000000007;
        int n = nums.length;
        int m = 0;
        for (int i = 0; i < n; i++) {
            m = Math.max(nums[i], m);
        }

        // init dp -- focus on arr1
        // dp[i][j] ith element of nums, j previous num
        int[][] dp = new int[n][m + 1];
        for (int i = 0; i <= nums[0]; i++) {
            dp[0][i] = 1;
        }

        // iterate dp
        for (int i = 1; i < n; i++) {
            // caculate prefix Sum
            long[] prefixSum = new long[m + 1];
            prefixSum[0] = (long) dp[i - 1][0];
            for (int j = 1; j < m + 1; j++) {
                prefixSum[j] = (prefixSum[j - 1] + dp[i - 1][j]) % MOD;
            }

            for (int j = 0; j <= nums[i]; j++) {
                int max = Math.min(j, nums[i - 1] - nums[i] + j);
                dp[i][j] = (max >= 0 ? (int) (prefixSum[max] % MOD) : 0);
            }
        }

        long sum = 0;
        for (int i = 0; i < m + 1; i++) {
            sum += dp[n - 1][i];
            sum %= MOD;
        }

        return (int) sum % MOD;
    }
}