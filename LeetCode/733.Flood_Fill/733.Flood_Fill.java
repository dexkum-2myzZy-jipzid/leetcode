class Solution {
    boolean[][] visited;

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int m = image.length, n = image[0].length;
        visited = new boolean[m][n];

        scatter4Directions(image, sr, sc, color, image[sr][sc]);

        return image;
    }

    private void scatter4Directions(int[][] image, int i, int j, int color, int num) {
        if (i < 0 || i >= image.length || j < 0 || j >= image[0].length || visited[i][j])
            return;

        if (image[i][j] == num) {
            image[i][j] = color;
            visited[i][j] = true;
            scatter4Directions(image, i - 1, j, color, num);
            scatter4Directions(image, i + 1, j, color, num);
            scatter4Directions(image, i, j - 1, color, num);
            scatter4Directions(image, i, j + 1, color, num);
        }
    }
}