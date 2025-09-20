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
    public int rob(TreeNode root) {
        int[] dp = helper(root, new int[2]);
        return Math.max(dp[0], dp[1]);
    }

    // dp[0]: not rob, dp[1]: rob
    private int[] helper(TreeNode node, int[] dp) {
        if (node == null) {
            return new int[2];
        }

        int[] left = helper(node.left, dp);
        int[] right = helper(node.right, dp);

        int[] next = new int[2];
        next[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        next[1] = node.val + left[0] + right[0];

        return next;
    }
}