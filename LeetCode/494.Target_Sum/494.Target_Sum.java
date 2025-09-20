class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }

        if (target > sum || target < -sum)
            return 0;
        if ((target + sum) % 2 != 0)
            return 0;

        // pos + neg = sum
        // pos - neg = target
        int pos = (sum + target) / 2;
        int[] dp = new int[pos + 1];
        dp[0] = 1;

        for (int i = 0; i < nums.length; i++) {
            for (int j = pos; j - nums[i] >= 0; j--) {
                dp[j] = dp[j - nums[i]] + dp[j];
            }
        }
        return dp[pos];
    }
}