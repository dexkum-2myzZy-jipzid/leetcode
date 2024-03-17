class Solution {
    public long countSubstrings(String s, char c) {
        char[] chs = s.toCharArray();
        int n = s.length();

        int[] cnt = new int[n];

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (chs[i] == c) {
                count += 1;
                cnt[i] = count;
            }
        }

        long res = 0;
        for (int i = 0; i < n; i++) {
            if (cnt[i] > 0) {
                res += (count - cnt[i]);
            }
        }
        res += count;
        return res;
    }
}