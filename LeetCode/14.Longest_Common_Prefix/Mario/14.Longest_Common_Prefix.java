class Solution {
    public String longestCommonPrefix(String[] strs) {
        // set strs[0] as Prefix, then compare the next
        // if common prefix is "", return it
        // if not, continue compare the next, unitl the last one

        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            String cur = strs[i];
            while (cur.indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix;
    }
}