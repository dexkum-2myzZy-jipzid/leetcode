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

// same way, using backtracking, but more effecient
class Solution {
    public boolean exist(char[][] board, String word) {
        // Convert the word to a byte array for easier manipulation
        byte[] wordAsBytes = word.getBytes();

        // If the word is longer than the total number of cells in the board, it cannot
        // be formed
        if (wordAsBytes.length > board.length * board[0].length) {
            return false;
        }

        // Initialize a frequency array to count the occurrences of each letter in the
        // board
        byte[] letterFrequencies = new byte[58];

        // Count the occurrences of each letter in the board
        for (char[] chars : board) {
            for (int j = 0; j < board[0].length; j++) {
                letterFrequencies[chars[j] - 'A'] += 1;
            }
        }

        // Check if the word can be formed with the letters in the board
        for (byte currentByte : wordAsBytes) {
            letterFrequencies[currentByte - 'A'] -= 1;
            // If a letter in the word is not present in the board, return false
            if (letterFrequencies[currentByte - 'A'] < 0) {
                return false;
            }
        }

        // Check if the word exists in the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                // If the first letter of the word is found in the board, start the recursive
                // search
                if (board[i][j] == wordAsBytes[0] && exist(board, wordAsBytes, i, j, 1)) {
                    return true;
                }
            }
        }
        // If the word is not found, return false
        return false;
    }

    private static boolean exist(char[][] board, byte[] wordAsBytes, int x, int y, int currentIndex) {
        // If we've reached the end of the word, it means the word exists in the board
        if (currentIndex == wordAsBytes.length) {
            return true;
        }
        // Mark the current cell as visited
        board[x][y] = '0';

        // Check each direction (up, left, down, right) to see if the next character in
        // the word is there
        if (x > 0 && board[x - 1][y] == wordAsBytes[currentIndex]) {
            if (exist(board, wordAsBytes, x - 1, y, currentIndex + 1)) {
                return true;
            }
        }
        if (y > 0 && board[x][y - 1] == wordAsBytes[currentIndex]) {
            if (exist(board, wordAsBytes, x, y - 1, currentIndex + 1)) {
                return true;
            }
        }
        if (x < board.length - 1 && board[x + 1][y] == wordAsBytes[currentIndex]) {
            if (exist(board, wordAsBytes, x + 1, y, currentIndex + 1)) {
                return true;
            }
        }
        if (y < board[0].length - 1 && board[x][y + 1] == wordAsBytes[currentIndex]) {
            if (exist(board, wordAsBytes, x, y + 1, currentIndex + 1)) {
                return true;
            }
        }
        // If we've checked all directions and none of them contained the next
        // character, backtrack and unmark the current cell
        board[x][y] = (char) wordAsBytes[currentIndex - 1];
        return false;
    }

}