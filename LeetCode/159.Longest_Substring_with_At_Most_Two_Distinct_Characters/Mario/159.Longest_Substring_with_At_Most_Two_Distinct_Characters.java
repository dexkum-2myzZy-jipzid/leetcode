class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        // Store character and its most recent position
        Map<Character, Integer> counter = new HashMap<>();
        char[] chs = s.toCharArray();

        int i = 0;
        int maxLen = 1;
        counter.put(chs[i], i);
        for (int j = 1; j < chs.length; j++) {
            counter.put(chs[j], j);
            if (counter.size() <= 2) {
                maxLen = Math.max(maxLen, j - i + 1);
            } else {
                while (i < j && counter.get(chs[i]) != i) {
                    i += 1;
                }
                counter.remove(chs[i]);
                i += 1;
            }
        }

        return maxLen;
    }
}