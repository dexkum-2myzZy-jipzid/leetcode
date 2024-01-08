class Solution {
    private final char[][] combinations = new char[][] { {}, {}, { 'a', 'b', 'c' }, { 'd', 'e', 'f' },
            { 'g', 'h', 'i' }, { 'j', 'k', 'l' }, { 'm', 'n', 'o' }, { 'p', 'q', 'r', 's' }, { 't', 'u', 'v' },
            { 'w', 'x', 'y', 'z' } };
    private List<String> res;

    public List<String> letterCombinations(String digits) {
        res = new ArrayList<>();
        if (digits.length() == 0) {
            return res;
        }
        backtracking(digits, new StringBuilder(), 0);
        return res;
    }

    private void backtracking(String str, StringBuilder builder, int index) {
        if (index == str.length()) {
            res.add(builder.toString());
            return;
        }

        char ch = str.charAt(index);
        char[] array = combinations[ch - '0'];
        for (char l : array) {
            builder.append(l);
            backtracking(str, builder, index + 1);
            builder.deleteCharAt(builder.length() - 1);
        }
    }
}