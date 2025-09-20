class Solution {
    private int index = 0;

    public boolean verifyPreorder(int[] nums) {
        // Reset the index to 0 for each new call
        index = 0;
        // Start the recursive check with the full integer range
        return isPreOrder(nums, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    // Checks if the given subarray is a valid BST preorder traversal.
    private boolean isPreOrder(int[] nums, int min, int max) {
        if (index >= nums.length) {
            return true;
        }

        int value = nums[index];
        if (min < value && value < max) {
            index += 1;
            // Recursively check the left subtree (values less than the current value)
            // and the right subtree (values greater than the current value)
            return isPreOrder(nums, min, value) || isPreOrder(nums, value, max);
        }

        return false;
    }
}