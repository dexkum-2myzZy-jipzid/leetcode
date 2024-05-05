class Solution {
    public int minAnagramLength(String s) {
        int n = s.length();
        char[] chs = s.toCharArray();
        for (int i = 1; i <= n / 2 + 1; i++) {
            if (n % i == 0) {
                if (helper(chs, i)) {
                    return i;
                }
            }
        }
        return n;
    }

    private boolean helper(char[] chs, int len) {
        int[] counter = new int[26];
        for (int i = 0; i < len; i++) {
            counter[chs[i] - 'a'] += 1;
        }

        int i = len;
        int[] curr = new int[26];
        while (i < chs.length) {
            Arrays.fill(curr, 0);
            for (int j = i; j < i + len; j++) {
                curr[chs[j] - 'a'] += 1;
            }
            if (Arrays.compare(counter, curr) != 0) {
                return false;
            }
            i += len;
        }
        return true;
    }
}