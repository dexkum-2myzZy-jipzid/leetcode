class Solution {
    public String minWindow(String s, String t) {

        int[] counter = new int[128];
        for (char c : t.toCharArray()) {
            counter[c] += 1;
        }

        int count = t.length();
        int start = 0, end = 0;
        int minLen = Integer.MAX_VALUE;
        int startIndex = 0;

        char[] chars = s.toCharArray();

        while (end < chars.length) {
            char ch = chars[end];
            if (counter[ch] > 0) {
                count--;
            }
            end += 1;
            counter[ch] -= 1;

            // find all characters in t
            while (count == 0) {
                // update startIndex & minLen
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }

                char c = chars[start];
                start += 1;
                counter[c] += 1;
                if (counter[c] > 0) {
                    count++;
                }
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : new String(chars, startIndex, minLen);
    }
}