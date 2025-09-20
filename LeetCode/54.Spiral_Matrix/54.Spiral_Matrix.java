class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;

        List<Integer> res = new ArrayList<>();
        int x = 0, y = 0;
        res.add(matrix[x][y]);
        int right = n, down = m, left = 0, up = 0;
        while (res.size() < m * n) {
            // left -> right
            while (res.size() < m * n && y + 1 < right) {
                y += 1;
                res.add(matrix[x][y]);
            }
            up += 1;

            // up -> down
            while (res.size() < m * n && x + 1 < down) {
                x += 1;
                res.add(matrix[x][y]);
            }
            right -= 1;

            // right -> left
            while (res.size() < m * n && y - 1 >= left) {
                y -= 1;
                res.add(matrix[x][y]);
            }
            down -= 1;

            // down -> up
            while (res.size() < m * n && x - 1 >= up) {
                x -= 1;
                res.add(matrix[x][y]);
            }
            left += 1;
        }

        return res;
    }

}