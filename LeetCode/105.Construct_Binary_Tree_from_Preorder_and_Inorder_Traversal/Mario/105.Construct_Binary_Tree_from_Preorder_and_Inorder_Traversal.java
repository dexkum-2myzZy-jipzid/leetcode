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

    private Map<Integer, Integer> map;
    private int index;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        index = 0;
        map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i], i);
        }
        return dfs(preorder, 0, preorder.length - 1);
    }

    public TreeNode dfs(int[] pre, int left, int right) {
        if (left > right)
            return null;

        int val = pre[index];
        index += 1;
        TreeNode node = new TreeNode(val);
        int mid = map.get(val);
        node.left = dfs(pre, left, mid - 1);
        node.right = dfs(pre, mid + 1, right);
        return node;
    }
}