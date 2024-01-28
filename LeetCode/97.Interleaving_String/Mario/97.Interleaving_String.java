class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length(), m = s2.length();
        if (n + m != s3.length())
            return false;
        boolean[][] dp = new boolean[n + 1][m + 1];
        dp[0][0] = true;

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        char[] arr3 = s3.toCharArray();

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                } else if (i == 0) {
                    if (dp[i][j - 1] && arr2[j - 1] == arr3[j - 1]) {
                        dp[i][j] = true;
                    }
                } else if (j == 0) {
                    if (dp[i - 1][j] && arr1[i - 1] == arr3[i - 1]) {
                        dp[i][j] = true;
                    }
                } else {
                    dp[i][j] = (dp[i - 1][j] && arr1[i - 1] == arr3[j + i - 1])
                            || (dp[i][j - 1] && arr2[j - 1] == arr3[j + i - 1]);
                }
            }
        }

        return dp[n][m];
    }

}