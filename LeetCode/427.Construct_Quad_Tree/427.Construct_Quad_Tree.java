/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};
*/

class Solution {
    public Node construct(int[][] grid) {
        return createquad(grid, 0, grid.length - 1, 0, grid.length - 1);
    }

    private Node createquad(int[][] grid, int rs, int re, int cs, int ce) {
        if (rs > re || cs > ce) {
            return null;
        }

        boolean isLeaf = true;
        int val = grid[rs][cs];
        for (int i = rs; i <= re; i++) {
            for (int j = cs; j <= ce; j++) {
                if (grid[i][j] != val) {
                    isLeaf = false;
                    break;
                }
            }
            if (!isLeaf)
                break;
        }

        if (isLeaf)
            return new Node(val == 1, true);

        int rm = (rs + re) / 2;
        int cm = (cs + ce) / 2;
        Node topLeft = createquad(grid, rs, rm, cs, cm);
        Node topRight = createquad(grid, rs, rm, cm + 1, ce);
        Node bottomLeft = createquad(grid, rm + 1, re, cs, cm);
        Node bottomRight = createquad(grid, rm + 1, re, cm + 1, ce);

        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}