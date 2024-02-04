class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        int[] counter = new int[128];

        for (char c : s.toCharArray()) {
            counter[c] += 1;
        }

        for (char c : t.toCharArray()) {
            counter[c] -= 1;
            if (counter[c] < 0) {
                return false;
            }
        }

        return true;
    }
}