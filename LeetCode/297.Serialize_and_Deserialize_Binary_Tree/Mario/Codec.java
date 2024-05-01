/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private StringBuilder rserialize(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("null,");
        } else {
            sb.append(String.valueOf(root.val)).append(",");
            sb = rserialize(root.left, sb);
            sb = rserialize(root.right, sb);
        }
        return sb;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = rserialize(root, new StringBuilder());
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    private int i = 0;

    public TreeNode deserialize(String data) {
        String[] array = data.split(",");
        return rdeserialize(array);
    }

    private TreeNode rdeserialize(String[] strs) {
        if (strs[i].equals("null")) {
            i++;
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(strs[i]));
        i += 1;
        root.left = rdeserialize(strs);
        root.right = rdeserialize(strs);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));