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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, null, null);
    }

    private boolean dfs(TreeNode node, Integer maxValue, Integer minValue) {
        if (node == null)
            return true;
        if ((minValue == null || node.val > minValue) && (maxValue == null || node.val < maxValue)) {
            return dfs(node.left, node.val, minValue) && dfs(node.right, maxValue, node.val);
        }
        return false;
    }
}