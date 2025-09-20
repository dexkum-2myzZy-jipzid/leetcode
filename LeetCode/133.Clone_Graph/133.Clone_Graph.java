class Solution {

    private Map<Integer, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null)
            return null;
        if (node.neighbors.size() == 0)
            return new Node(node.val);

        Node copy = new Node(node.val);
        map.put(node.val, copy);
        copyNode(node, copy);
        return copy;
    }

    private void copyNode(Node node, Node copy) {
        int n = node.neighbors.size();
        for (int i = 0; i < n; i++) {
            Node a = node.neighbors.get(i);
            if (!map.containsKey(a.val)) {
                Node aa = new Node(a.val);
                copy.neighbors.add(aa);
                map.put(a.val, aa);
                copyNode(a, aa);
            } else {
                copy.neighbors.add(map.get(a.val));
            }
        }
    }

}