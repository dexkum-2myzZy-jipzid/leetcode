class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();

        if (root != null)
            queue.offer(root);

        List<List<Integer>> res = new ArrayList<>();

        while (!queue.isEmpty()) {
            int n = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }
            res.add(level);
        }
        return res;
    }
}

// Another way
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<>();
        traverseNode(root, 0, ret);
        return ret;
    }

    private void traverseNode(TreeNode node, int level, List<List<Integer>> list) {
        if (node == null)
            return;
        if (list.size() <= level)
            list.add(new ArrayList<>());
        list.get(level).add(node.val);
        traverseNode(node.left, level + 1, list);
        traverseNode(node.right, level + 1, list);
    }
}