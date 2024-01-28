class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];

        int maxLen = 1;
        int begin = 0;
        char[] chars = s.toCharArray();

        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            if (i + 1 < n && chars[i] == chars[i + 1]) {
                dp[i][i + 1] = true;
                begin = i;
                maxLen = 2;
            }
        }

        for (int len = 3; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (chars[i] == chars[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    begin = i;
                    maxLen = len;
                }
            }
        }

        return s.substring(begin, begin + maxLen);

    }
}