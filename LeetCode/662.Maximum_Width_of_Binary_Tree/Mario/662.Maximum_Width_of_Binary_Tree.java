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
    public int widthOfBinaryTree(TreeNode root) {
        record Pair(TreeNode node, int val) {
        }
        ;

        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 1));

        int result = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            int leftmostVal = -1;
            for (int i = 0; i < size; i++) {
                Pair p = queue.poll();
                TreeNode node = p.node;
                int val = p.val;

                if (leftmostVal == -1) {
                    leftmostVal = val;
                } else {
                    result = Math.max(result, val - leftmostVal + 1);
                }

                if (node.left != null) {
                    queue.offer(new Pair(node.left, val * 2));
                }
                if (node.right != null) {
                    queue.offer(new Pair(node.right, val * 2 + 1));
                }
            }
        }

        return result;
    }
}