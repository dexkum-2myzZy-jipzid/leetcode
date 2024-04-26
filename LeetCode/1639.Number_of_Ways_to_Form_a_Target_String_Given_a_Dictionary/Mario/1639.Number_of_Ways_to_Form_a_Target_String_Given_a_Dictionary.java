class Solution {
    public int numWays(String[] words, String target) {
        final int M = 1_000_000_007;
        int n = target.length(), m = words[0].length();
        int[][] counter = new int[26][m + 1];

        for (String word : words) {
            for (int i = 0; i < m; i++) {
                counter[word.charAt(i) - 'a'][i + 1] += 1;
            }
        }

        // dp[i][j] : how many ways to form target[0:i] with counter[26][k];
        // not choose jth letter: dp[i][j] = dp[i]dp[j-1]
        // choose jth letter: dp[i][j] = dp[i-1]dp[j-1] * counter[x][k]
        long[][] dp = new long[n + 1][m + 1];

        // init
        for (int i = 0; i <= m; i++)
            dp[0][i] = 1;

        target = "#" + target;

        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= m; j++) {
                dp[i][j] = dp[i][j - 1];
                dp[i][j] %= M;
                if (counter[target.charAt(i) - 'a'][j] > 0) {
                    dp[i][j] += dp[i - 1][j - 1] * counter[target.charAt(i) - 'a'][j];
                    dp[i][j] %= M;
                }
            }
        }

        // for (long[] d : dp) {
        // System.out.println(Arrays.toString(d));
        // }

        return (int) dp[n][m];
    }
}