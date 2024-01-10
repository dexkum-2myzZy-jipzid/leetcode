class Solution {

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {
        backtracking(nums, 0);
        return res;
    }

    private void backtracking(int[] nums, int start) {
        if (nums.length == start) {
            ArrayList permutation = new ArrayList<>();
            for (int num : nums) {
                permutation.add(num);
            }
            res.add(permutation);
            return;
        }

        for (int i = start; i < nums.length; i++) {
            swap(nums, i, start);
            // System.out.println("nums:" + Arrays.toString(nums));
            backtracking(nums, start + 1);
            swap(nums, start, i);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}