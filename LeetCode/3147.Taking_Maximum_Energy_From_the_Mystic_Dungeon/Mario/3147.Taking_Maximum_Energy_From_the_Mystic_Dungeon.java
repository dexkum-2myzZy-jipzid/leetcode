class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int[] dp = new int[energy.length];

        // init dp
        for (int i = 0; i < k; i++) {
            dp[i] = energy[i];
        }

        for (int i = k; i < energy.length; i++) {
            dp[i] = Math.max(energy[i], energy[i] + dp[i - k]);
        }

        int result = Integer.MIN_VALUE;
        for (int i = energy.length - k; i < energy.length; i++) {
            result = Math.max(result, dp[i]);
        }

        return result;
    }
}