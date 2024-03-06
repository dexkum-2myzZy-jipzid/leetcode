class Solution {
    public boolean isSubsequence(String s, String t) {
        int n = s.length(), m = t.length();
        int[][] dp = new int[n + 1][m + 1];

        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (sc[i - 1] == tc[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i][j - 1];
                }
            }
        }

        return dp[n][m] == n ? true : false;
    }
}