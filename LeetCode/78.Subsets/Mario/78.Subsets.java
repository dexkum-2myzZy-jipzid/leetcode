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