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

    private int maxValue = -1001;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxValue;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftMax = dfs(node.left);
        int rightMax = dfs(node.right);
        leftMax = Math.max(leftMax, 0);
        rightMax = Math.max(rightMax, 0);

        maxValue = Math.max(maxValue, leftMax + rightMax + node.val);

        return Math.max(leftMax, rightMax) + node.val;
    }
}