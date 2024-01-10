class Solution {

    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backtracking(new ArrayList<Integer>(), candidates, 0, target, 0);
        return res;
    }

    private void backtracking(ArrayList<Integer> nums, int[] candidates, int sum, int target, int start) {
        if (sum >= target) {
            if (sum == target) {
                res.add(new ArrayList<>(nums));
            }
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            nums.add(candidates[i]);
            backtracking(nums, candidates, sum + candidates[i], target, i);
            nums.remove(nums.size() - 1);
        }
    }
}