class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = (obstacleGrid[0][0] == 1) ? 0 : 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0)
                    continue;

                if (i == 0) {
                    dp[i][j] = (obstacleGrid[i][j] == 1) ? 0 : dp[i][j - 1];
                } else if (j == 0) {
                    dp[i][j] = (obstacleGrid[i][j] == 1) ? 0 : dp[i - 1][j];
                } else {
                    dp[i][j] = (obstacleGrid[i][j] == 1) ? 0 : dp[i][j - 1] + dp[i - 1][j];
                }
            }
        }

        return dp[m - 1][n - 1];
    }
}