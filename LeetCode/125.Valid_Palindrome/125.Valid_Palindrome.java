class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        String lowerS = s.toLowerCase();
        for (int i = 0; i < lowerS.length(); i++) {
            char ch = lowerS.charAt(i);
            if (Character.isLetterOrDigit(ch)) {
                sb.append(ch);
            }
        }
        String str = sb.toString();
        int left = 0, right = str.length() - 1;
        while (left <= right) {
            if (str.charAt(left) == str.charAt(right)) {
                left += 1;
                right -= 1;
            } else {
                return false;
            }
        }
        return true;
    }
}