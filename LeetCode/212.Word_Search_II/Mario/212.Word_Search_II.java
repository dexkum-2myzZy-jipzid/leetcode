class Solution {

    private int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
    private Set<String> res = new HashSet<String>();

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            root.insert(word);
        }

        int m = board.length;
        int n = (board.length > 0) ? board[0].length : 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(i, j, m, n, board, root);
            }
        }

        return new ArrayList<String>(res);
    }

    private void dfs(int i, int j, int m, int n, char[][] board, TrieNode cur) {
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return;
        }

        char ch = board[i][j];
        int index = ch - 'a';
        if (ch != '#' && cur.children[index] != null) {
            TrieNode node = cur.children[index];
            if (node.word != "") {
                res.add(node.word);
            }
            board[i][j] = '#';
            for (int[] dir : dirs) {
                dfs(i + dir[0], j + dir[1], m, n, board, node);
            }
            board[i][j] = ch;
        }
        return;
    }

}

class TrieNode {
    public String word;
    public TrieNode[] children;

    public TrieNode() {
        word = "";
        children = new TrieNode[26];
    }

    public void insert(String word) {
        TrieNode cur = this;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            if (cur.children[index] == null) {
                cur.children[index] = new TrieNode();
            }
            cur = cur.children[index];
        }
        cur.word = word;
    }
}