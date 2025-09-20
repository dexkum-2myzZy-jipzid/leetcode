/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        // create tree
        TreeNode root = createTree(nums, 0, nums.length - 1);
        return root;
    }

    private TreeNode createTree(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        int index = (end + start) / 2;
        int num = nums[index];
        TreeNode node = new TreeNode(num);
        node.left = createTree(nums, start, index - 1);
        node.right = createTree(nums, index + 1, end);
        return node;
    }
}