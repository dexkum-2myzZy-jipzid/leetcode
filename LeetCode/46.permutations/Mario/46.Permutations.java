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

// use visited array to record the visited element
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtracking(res, nums, new ArrayList<Integer>());
        return res;
    }

    private void backtracking(List<List<Integer>> res, int[] nums, List<Integer> curr) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!curr.contains(nums[i])) {
                curr.add(nums[i]);
                backtracking(res, nums, curr);
                curr.remove(curr.size() - 1);
            }
        }
    }
}