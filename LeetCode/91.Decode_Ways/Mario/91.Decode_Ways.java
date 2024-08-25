class Solution {
    char[] chs;
    int[] memo;

    public int numDecodings(String s) {
        chs = s.toCharArray();
        memo = new int[chs.length];
        Arrays.fill(memo, -1);
        return dfs(0);
    }

    private int dfs(int index) {
        if (chs.length == index) {
            return 1;
        }

        if (memo[index] >= 0) {
            return memo[index];
        }

        if (chs[index] == '0') {
            return 0;
        }

        int count = 0;
        count += dfs(index + 1);
        if (index + 1 < chs.length) {
            int num = (chs[index] - '0') * 10 + (chs[index + 1] - '0');
            if (num <= 26) {
                count += dfs(index + 2);
            }
        }

        memo[index] = count;
        return count;
    }
}

// dp
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];

        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        if (dp[1] == 0) {
            return 0;
        }

        // dp[i]: ways of s[0:i] can decode
        for (int i = 2; i <= n; i++) {
            if (s.charAt(i - 1) != '0') {
                dp[i] = dp[i - 1];
            }

            int num = (s.charAt(i - 2) - '0') * 10 + s.charAt(i - 1) - '0';
            if (num <= 26 && num >= 10) {
                dp[i] += dp[i - 2];
            }
        }

        // System.out.println(Arrays.toString(dp));

        return dp[n];
    }
}