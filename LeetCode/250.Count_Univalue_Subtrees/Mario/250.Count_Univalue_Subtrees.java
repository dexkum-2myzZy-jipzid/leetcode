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

    private static int count = 0;

    public int countUnivalSubtrees(TreeNode root) {
        // Reset the count to 0 for each new solution call
        count = 0;

        isUniSubtree(root);

        return count;
    }

    private int isUniSubtree(TreeNode node) {
        if (node == null)
            return Integer.MAX_VALUE;

        // If the node is a leaf node, it is a uni-value subtree.
        if (node.left == null && node.right == null) {
            count += 1;
            return node.val;
        }

        // Check if the left and right subtrees are uni-value subtrees.
        int left = isUniSubtree(node.left);
        int right = isUniSubtree(node.right);

        // If the node has only one child, check if it is a uni-value subtree.
        if (node.left == null) {
            if (right != Integer.MAX_VALUE && right == node.val) {
                count += 1;
                return node.val;
            }
        } else if (node.right == null) {
            if (left != Integer.MAX_VALUE && left == node.val) {
                count += 1;
                return node.val;
            }
        } else {
            // If the node has two children, check if it is a uni-value subtree.
            if (node.val == left && node.val == right) {
                count += 1;
                return node.val;
            }
        }
        return Integer.MAX_VALUE;
    }

}