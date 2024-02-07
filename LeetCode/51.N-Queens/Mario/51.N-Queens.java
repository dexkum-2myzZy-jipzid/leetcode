class Solution {
    private List<List<String>> res;

    public List<List<String>> solveNQueens(int n) {
        res = new ArrayList<>();
        boolean[] cols = new boolean[n], diag1 = new boolean[2 * n], diag2 = new boolean[2 * n];
        backtrack(n, 0, cols, diag1, diag2, new ArrayList<String>());
        return res;
    }

    private void backtrack(int n, int i, boolean[] cols, boolean[] diag1, boolean[] diag2, List<String> strs) {
        if (i == n) {
            res.add(new ArrayList(strs));
            return;
        }

        for (int j = 0; j < cols.length; j++) {
            if (cols[j] || diag1[i + j] || diag2[i - j + n])
                continue;

            cols[j] = diag1[i + j] = diag2[i - j + n] = true;
            strs.add(buildRow(n, j));
            backtrack(n, i + 1, cols, diag1, diag2, strs);
            cols[j] = diag1[i + j] = diag2[i - j + n] = false;
            strs.removeLast();
        }

    }

    private String buildRow(int n, int j) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(i == j ? 'Q' : '.');
        }
        return sb.toString();
    }
}