class Solution {

    class Point {
        int x, y;
        double dis;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.dis = Math.pow(x, 2) + Math.pow(y, 2);
        }
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> maxHeap = new PriorityQueue<>((p1, p2) -> Double.compare(p1.dis, p2.dis));
        for (int[] p : points) {
            maxHeap.offer(new Point(p[0], p[1]));
        }

        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++) {
            Point p = maxHeap.poll();
            res[i][0] = p.x;
            res[i][1] = p.y;
        }
        return res;
    }
}