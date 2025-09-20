class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i < strs.length; i++) {
            String str = strs[i];
            int ones = getTheNumOfOnes(str);
            int zeros = str.length() - ones;
            for (int j = m; j >= zeros; j--) {
                for (int k = n; k >= ones; k--) {
                    dp[j][k] = Math.max(dp[j][k], dp[j - zeros][k - ones] + 1);
                }
            }
        }

        return dp[m][n];
    }

    private int getTheNumOfOnes(String str) {
        char[] chars = str.toCharArray();
        int res = 0;
        for (char c : chars) {
            if (c == '1')
                res += 1;
        }
        return res;
    }
}