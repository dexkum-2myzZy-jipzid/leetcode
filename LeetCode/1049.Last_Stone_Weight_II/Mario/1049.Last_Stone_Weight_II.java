class Solution {
    public int lastStoneWeightII(int[] stones) {
        int n = stones.length;
        int sum = 0;
        for (int s : stones)
            sum += s;

        int t = sum / 2;
        int[] dp = new int[t + 1];
        for (int i = 0; i < n; i++) {
            for (int j = t; j >= stones[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }

        return sum - 2 * dp[t];
    }
}