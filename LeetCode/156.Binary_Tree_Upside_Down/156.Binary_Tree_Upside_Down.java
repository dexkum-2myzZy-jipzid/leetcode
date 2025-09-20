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

    public static TreeNode upsideDownBinaryTree(TreeNode root) {

        // get new root
        TreeNode newRoot = root;
        while (newRoot != null && newRoot.left != null) {
            newRoot = newRoot.left;
        }

        // Call helper method to turn the tree upside down
        turnUpsideDownBinaryTree(root);

        return newRoot;
    }

    // This method is a helper method to recursively turn the binary tree upside
    // down
    public static TreeNode turnUpsideDownBinaryTree(TreeNode root) {
        if (root == null)
            return null;
        // left node
        TreeNode left = turnUpsideDownBinaryTree(root.left);
        // current node
        if (left != null) {
            left.right = root;
            root.left = null;
            left.left = root.right;
            root.right = null;
        }
        return root;
    }
}