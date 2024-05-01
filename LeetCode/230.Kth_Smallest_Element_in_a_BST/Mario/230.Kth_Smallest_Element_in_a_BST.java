class Solution {
    // BST inorder traversal
    private List<Integer> list;

    public int kthSmallest(TreeNode root, int k) {
        list = new ArrayList<>();
        inorderTraversal(root, k);
        return list.get(k - 1);
    }

    private void inorderTraversal(TreeNode node, int k) {
        if (node == null || list.size() >= k)
            return;
        inorderTraversal(node.left, k);
        list.add(node.val);
        inorderTraversal(node.right, k);
    }
}