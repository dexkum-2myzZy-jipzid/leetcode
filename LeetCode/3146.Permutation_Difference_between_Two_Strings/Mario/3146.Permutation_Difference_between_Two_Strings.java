class Solution {
    public int findPermutationDifference(String s, String t) {
        // map store char in s
        Map<Character, Integer> map = new HashMap<>();
        char[] sChars = s.toCharArray();
        for (int i = 0; i < sChars.length; i++) {
            map.put(sChars[i], i);
        }

        int result = 0;
        for (int i = 0; i < t.length(); i++) {
            int diff = Math.abs(i - map.get(t.charAt(i)));
            result += diff;
        }
        return result;
    }
}