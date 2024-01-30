class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        int[] pre = new int[26], suf = new int[26];
        boolean[][] dp = new boolean[26][26];
        for (int i = 0; i < n; i++) {
            suf[s.charAt(i) - 'a'] += 1;
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            int j = s.charAt(i) - 'a';
            suf[j] -= 1;
            for (int k = 0; k < 26; k++) {
                dp[k][j] |= (suf[k] >= 1 && pre[k] >= 1);
            }
            pre[j] += 1;
        }

        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++)
                if (dp[i][j])
                    res += 1;

        return res;
    }
}