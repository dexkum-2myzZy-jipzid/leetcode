class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();

        int n = s.length();
        char[] chars = s.toCharArray();
        int i = 0, j = 0;
        int res = 0;
        while (j < n) {
            char ch = chars[j];
            if (set.contains(ch)) {
                set.remove(chars[i]);
                i++;
            } else {
                set.add(ch);
                j++;
                res = Math.max(res, j - i);
            }
        }
        return res;
    }
}