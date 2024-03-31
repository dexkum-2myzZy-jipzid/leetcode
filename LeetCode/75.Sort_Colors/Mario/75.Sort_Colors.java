class Solution {
    public void sortColors(int[] nums) {
        int p0 = 0, p2 = nums.length - 1;
        int i = 0;
        while (i <= p2) {
            if (nums[i] == 0) {
                swap(nums, i, p0);
                p0 += 1;
                i += 1;
            } else if (nums[i] == 2) {
                swap(nums, i, p2);
                p2 -= 1;
            } else {
                i += 1;
            }
        }
    }

    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}