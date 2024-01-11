class Solution {

    private int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, -1 }, { 0, 1 } };

    public boolean exist(char[][] board, String word) {
        char ch = word.charAt(0);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == ch) {
                    if (backtrack(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean backtrack(char[][] b, String w, int i, int j, int start) {
        if (w.length() == start) {
            return true;
        }

        if (i < 0 || i >= b.length || j < 0 || j >= b[0].length) {
            return false;
        }

        char ch = w.charAt(start);
        if (ch == b[i][j]) {
            b[i][j] = '.';
            for (int[] dir : dirs) {
                if (backtrack(b, w, i + dir[0], j + dir[1], start + 1)) {
                    return true;
                }
            }
            b[i][j] = ch;
        }

        return false;
    }
}