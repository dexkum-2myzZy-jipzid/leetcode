class Solution {
    public String reversePrefix(String word, char ch) {
        int j = -1;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ch) {
                j = i;
                break;
            }
        }

        if (j == -1)
            return word;
        char[] chs = word.toCharArray();
        for (int i = 0; i <= j; i++, j--) {
            char tmp = chs[i];
            chs[i] = chs[j];
            chs[j] = tmp;
        }

        return String.valueOf(chs);
    }
}