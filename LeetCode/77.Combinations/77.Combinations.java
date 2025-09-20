class Solution {

    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        backtracking(new ArrayList<>(), k, 1, n);
        return res;
    }

    private void backtracking(List<Integer> list, int k, int range, int n) {
        if (k == 0) {
            res.add(new ArrayList<>(list));
            return;
        }

        for (int i = range; i <= n; i++) {
            list.add(i);
            backtracking(list, k - 1, i + 1, n);
            list.remove(list.size() - 1);
        }
    }
}