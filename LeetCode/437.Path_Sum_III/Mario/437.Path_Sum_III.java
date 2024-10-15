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
    private int count = 0;
    int target = 0;
    // store prefixSum and its count
    HashMap<Long, Integer> prefixSumMap = new HashMap<>();

    public int pathSum(TreeNode root, int targetSum) {
        // prefix sum + map
        target = targetSum;
        dfs(root, 0L);
        return count;
    }

    public void dfs(TreeNode node, long sum) {
        if (node == null) {
            return;
        }

        sum += node.val;

        if (sum == target) {
            count += 1;
        }

        count += prefixSumMap.getOrDefault(sum - target, 0);

        prefixSumMap.put(sum, prefixSumMap.getOrDefault(sum, 0) + 1);

        dfs(node.left, sum);
        dfs(node.right, sum);

        prefixSumMap.put(sum, prefixSumMap.get(sum) - 1);
    }
}