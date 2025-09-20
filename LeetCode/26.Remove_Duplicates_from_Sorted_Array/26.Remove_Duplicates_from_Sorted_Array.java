class Solution {
    public int removeDuplicates(int[] nums) {
        int pre = nums[0];
        int j = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != pre) {
                pre = nums[i];
                nums[j] = pre;
                j += 1;
            }
        }

        return j;
    }
}