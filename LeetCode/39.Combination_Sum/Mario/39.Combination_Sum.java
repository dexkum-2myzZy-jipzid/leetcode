class Solution {
    private List<List<Integer>> res;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        res = new ArrayList<>();
        backtracking(candidates, target, 0, new ArrayList<Integer>(), 0);
        return res;
    }

    private void backtracking(int[] cads, int target, int sum, List<Integer> list, int start) {
        if (target == sum) {
            res.add(new ArrayList<>(list));
            return;
        }

        for (int i = start; i < cads.length; i++) {
            if (sum + cads[i] > target) {
                continue;
            }
            list.add(cads[i]);
            backtracking(cads, target, sum + cads[i], list, i);
            list.remove(list.size() - 1);
        }
    }
}