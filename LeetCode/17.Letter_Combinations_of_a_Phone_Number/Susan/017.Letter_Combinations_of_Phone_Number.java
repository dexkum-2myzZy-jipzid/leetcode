class Solution {
    String[] mapping = new String[] { " ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
    List<String> res = new LinkedList<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return res;
        }

        bfs(digits, 0, new StringBuilder());
        return res;
    }

    public void bfs(String digits, int start, StringBuilder sb) {
        if (sb.length() == digits.length()) {
            res.add(sb.toString());
            return;
        }

        for (int i = start; i < digits.length(); i++) {
            int index = digits.charAt(i) - '0';
            for (char c : mapping[index].toCharArray()) {
                sb.append(c);
                bfs(digits, i + 1, sb);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }
}