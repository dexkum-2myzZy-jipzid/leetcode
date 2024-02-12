class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int num : nums)
            sum += num;
        if (sum % 2 == 1)
            return false;

        int t = sum / 2;
        int[] dp = new int[t + 1];

        for (int i = 0; i < n; i++) {
            for (int j = t; j >= nums[i]; j--) {
                dp[j] = Math.max(dp[j - nums[i]] + nums[i], dp[j]);
            }
            // System.out.println(Arrays.toString(dp));
        }

        return dp[t] == t;
    }
}