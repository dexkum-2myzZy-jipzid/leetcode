class Solution {
    public boolean makesquare(int[] matchsticks) {
        int sum = 0;
        int n = matchsticks.length;
        for (int i = 0; i < n; i++) {
            sum += matchsticks[i];
        }

        if (sum % 4 != 0) {
            return false;
        }
        Arrays.sort(matchsticks);
        for (int i = 0; i < n / 2; i++) {
            int tmp = matchsticks[i];
            matchsticks[i] = matchsticks[n - 1 - i];
            matchsticks[n - 1 - i] = tmp;
        }

        // knapsack dp
        // dp[i][j] ith matchsticks, j cumulative length
        int m = sum / 4;
        boolean[][] dp = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            int cur = matchsticks[i];
            if (cur > m) {
                return false;
            } else {
                dp[i][cur] = true;
            }
            for (int j = i - 1; j >= 0; j--) {
                if (matchsticks[j] + cur <= m) {

                }
            }
        }

    }
}