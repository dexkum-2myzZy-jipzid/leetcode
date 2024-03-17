class Solution {
    public boolean isSubstringPresent(String s) {

        char[] chars = s.toCharArray();
        int n = chars.length;

        for (int i = 1; i < n; i++) {
            char cur = chars[i], pre = chars[i - 1];
            if (cur == pre)
                return true;
            for (int j = 0; j < n; j++) {
                if (cur == chars[j] && j + 1 < n && chars[j + 1] == pre) {
                    return true;
                }
            }
        }

        return false;
    }
}