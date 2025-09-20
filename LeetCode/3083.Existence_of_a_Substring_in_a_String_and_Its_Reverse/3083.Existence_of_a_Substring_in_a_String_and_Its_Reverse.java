class Solution {
    public boolean isSubstringPresent(String s) {
        boolean[][] set = new boolean[26][26];
        char[] chs = s.toCharArray();

        for (int i = 0; i < chs.length - 1; i++) {
            int a = chs[i] - 'a', b = chs[i + 1] - 'a';
            set[a][b] = true;
            if (set[b][a]) {
                return true;
            }
        }
        return false;
    }
}