class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] matrix = new int[n][n];
        for (int[] row : matrix) {
            Arrays.fill(row, 10001);
        }
        for (int i = 0; i < n; i++) {
            matrix[i][i] = 0;
        }
        for (int[] edge : edges) {
            int v1 = edge[0], v2 = edge[1], w = edge[2];
            matrix[v1][v2] = w;
            matrix[v2][v1] = w;
        }

        // Floyd algorithm
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                }
            }
        }

        int city = 0, minNei = n;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] <= distanceThreshold) {
                    count += 1;
                }
                if (count > minNei)
                    break;
            }
            if (count <= minNei) {
                city = i;
                minNei = count;
            }
        }

        return city;
    }
}