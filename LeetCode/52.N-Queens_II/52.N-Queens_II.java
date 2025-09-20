class Solution {
    int res = 0;

    public int totalNQueens(int n) {
        Set<Integer> col = new HashSet<>();
        Set<Integer> posDiagonal = new HashSet<>();
        Set<Integer> negDiagonal = new HashSet<>();
        backtracking(n, 0, col, posDiagonal, negDiagonal);
        return res;
    }

    private void backtracking(int n, int r, Set<Integer> col, Set<Integer> posDiagonal, Set<Integer> negDiagonal) {
        if (r == n) {
            res += 1;
            return;
        }

        for (int c = 0; c < n; c++) {
            if (col.contains(c) || posDiagonal.contains(r + c) || negDiagonal.contains(r - c)) {
                continue;
            }
            col.add(c);
            posDiagonal.add(r + c);
            negDiagonal.add(r - c);
            backtracking(n, r + 1, col, posDiagonal, negDiagonal);
            col.remove(c);
            posDiagonal.remove(r + c);
            negDiagonal.remove(r - c);
        }
    }
}