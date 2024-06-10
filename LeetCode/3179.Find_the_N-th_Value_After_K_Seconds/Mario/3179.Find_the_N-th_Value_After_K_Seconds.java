class Solution {
    public int valueAfterKSeconds(int n, int k) {
        final int M = 1_000_000_007;
        int[][] dp = new int[k + 1][n];
        Arrays.fill(dp[0], 1);

        // for(int[] d: dp){
        // System.out.println(Arrays.toString(d));
        // }

        // iterate
        for (int i = 1; i < k + 1; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    dp[i][0] = 1;
                } else {
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % M;
                }
            }
        }

        // for(int[] d: dp){
        // System.out.println(Arrays.toString(d));
        // }

        return dp[k][n - 1];
    }
}