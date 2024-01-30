class Solution {
    private int[] nums, count;
    private int k, res = -1;

    public int beautifulSubsets(int[] nums, int k) {
        this.nums = nums;
        this.k = k;
        this.count = new int[1001 + 2 * k];
        backtrack(0);
        return res;
    }

    private void backtrack(int i) {
        if (nums.length == i) {
            res += 1;
            return;
        }

        // not add nums[i]
        backtrack(i + 1);

        // add nums[i]
        int x = nums[i] + k;
        if (count[x - k] == 0 && count[x + k] == 0) {
            count[x] += 1;
            backtrack(i + 1);
            count[x] -= 1;
        }
    }
}