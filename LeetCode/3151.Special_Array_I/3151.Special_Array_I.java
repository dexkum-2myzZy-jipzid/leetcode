class Solution {
    public boolean isArraySpecial(int[] nums) {
        if (nums.length <= 1) {
            return true;
        }

        for (int i = 1; i < nums.length; i++) {
            int pre = nums[i - 1], current = nums[i];
            if (pre % 2 == current % 2) {
                return false;
            }
        }

        return true;
    }
}