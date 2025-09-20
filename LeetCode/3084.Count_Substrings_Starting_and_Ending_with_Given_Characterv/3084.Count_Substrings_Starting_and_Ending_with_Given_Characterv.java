class Solution {
    public long countSubstrings(String s, char c) {
        char[] chs = s.toCharArray();

        long count = 0;
        for (char ch : chs) {
            if (ch == c)
                count += 1;
        }

        return count * (count + 1) / 2;
    }
}