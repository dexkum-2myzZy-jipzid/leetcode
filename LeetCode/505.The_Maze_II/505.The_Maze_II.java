class Solution {

    static class Point {
        int x;
        int y;
        int path;

        public Point(int x, int y, int path) {
            this.x = x;
            this.y = y;
            this.path = path;
        }

        // check if two points are equal
        public boolean equal(Point other) {
            return this.x == other.x && this.y == other.y;
        }

        @Override
        public String toString() {
            return this.x + "|" + this.y;
        }
    }

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        // store the points in the maze
        PriorityQueue<Point> heap = new PriorityQueue<>((p1, p2) -> p1.path - p2.path);

        int[][] distance = new int[maze.length][maze[0].length];
        for (int[] row : distance)
            Arrays.fill(row, Integer.MAX_VALUE);

        // four possible directions
        int[][] directions = new int[][] { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

        // Start point
        Point startPoint = new Point(start[0], start[1], 0);
        heap.offer(startPoint);

        // Destination point
        Point dest = new Point(destination[0], destination[1], 0);

        while (!heap.isEmpty()) {
            // Poll the point with the shortest path
            Point current = heap.poll();

            if (distance[current.x][current.y] < current.path) {
                continue;
            }

            // For each direction
            for (int[] direction : directions) {
                // next point
                int nextX = current.x + direction[0], nextY = current.y + direction[1];
                int path = 0;

                // While the next point is valid and not a wall
                while (isValid(nextX, nextY, maze) && maze[nextX][nextY] == 0) {
                    path += 1;
                    nextX += direction[0];
                    nextY += direction[1];
                }

                Point next = new Point(nextX - direction[0], nextY - direction[1], path + current.path);
                if (distance[current.x][current.y] + path < distance[next.x][next.y]) {
                    distance[next.x][next.y] = next.path;
                    heap.offer(next);
                }
            }
        }

        // If the destination cannot be reached, return -1
        return distance[dest.x][dest.y] == Integer.MAX_VALUE ? -1 : distance[dest.x][dest.y];
    }

    private boolean isValid(int x, int y, int[][] maze) {
        return x >= 0 && x < maze.length && y >= 0 && y < maze[0].length;
    }
}