class Solution {
    public int longestPalindrome(String s) {
        int[] counter = new int[128];

        for (char ch : s.toCharArray()) {
            counter[ch] += 1;
        }

        int result = 0;
        boolean oddNum = false;
        for (int num : counter) {
            result += num / 2 * 2;
            if (!oddNum && num % 2 == 1) {
                oddNum = true;
            }
        }
        if (oddNum)
            result += 1;

        return result;
    }
}