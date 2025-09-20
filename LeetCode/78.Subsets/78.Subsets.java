class Solution {

    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0, new ArrayList<Integer>());
        return res;
    }

    private void backtrack(int[] nums, int index, List<Integer> array) {
        if (nums.length == index) {
            res.add(new ArrayList<>(array));
        } else {
            // not put num into array
            backtrack(nums, index + 1, array);

            // put num into array
            array.add(nums[index]);
            backtrack(nums, index + 1, array);
            array.remove(array.size() - 1);
        }
    }
}

// different backtracking solution
class Solution {
    private List<List<Integer>> res;

    public List<List<Integer>> subsets(int[] nums) {
        res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i <= n; i++) {
            backtracking(i, 0, new ArrayList<>(), nums);
        }
        return res;
    }

    private void backtracking(int arrSize, int start, List<Integer> arr, int[] nums) {
        if (arrSize == arr.size()) {
            res.add(new ArrayList<>(arr));
            return;
        }

        for (int i = start; i < nums.length; i++) {
            arr.add(nums[i]);
            backtracking(arrSize, i + 1, arr, nums);
            arr.remove(arr.size() - 1);
        }
    }
}