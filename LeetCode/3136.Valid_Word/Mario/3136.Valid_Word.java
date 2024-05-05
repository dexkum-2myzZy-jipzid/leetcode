class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3) {
            return false;
        }

        boolean vowel = false, consonant = false;
        char[] chs = word.toCharArray();
        for (int i = 0; i < chs.length; i++) {
            char ch = chs[i];
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I'
                    || ch == 'O' || ch == 'U') {
                vowel = true;
            } else if (ch >= 65 && ch <= 90 || ch >= 97 && ch <= 122) {
                consonant = true;
            } else if (ch >= '0' && ch <= '9') {
                continue;
            } else {
                return false;
            }
        }
        if (vowel && consonant) {
            return true;
        }
        return false;
    }
}