class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int max = 1;

        for (int i = 0; i < nums.length; i++) {
            int localMax = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    localMax = Math.max(localMax, dp[j] + 1);
                }
            }
            dp[i] = localMax;
            if (localMax > max)
                max = localMax;
        }
        return max;
    }
}