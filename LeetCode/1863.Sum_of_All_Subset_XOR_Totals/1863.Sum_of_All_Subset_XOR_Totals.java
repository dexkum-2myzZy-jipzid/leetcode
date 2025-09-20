class Solution {
    public int subsetXORSum(int[] nums) {
        return dfs(nums, 0, 0);
    }

    // pick current num or not pick current num
    private int dfs(int[] nums, int index, int xorVal) {
        if (nums.length == index) {
            return xorVal;
        }

        int result = 0;
        // pick current num
        result += dfs(nums, index + 1, xorVal ^ nums[index]);
        // not pick current num
        result += dfs(nums, index + 1, xorVal);

        return result;
    }
}