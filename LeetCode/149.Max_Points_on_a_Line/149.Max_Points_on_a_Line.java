class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n < 3)
            return n;

        int max = 2;
        for (int i = 0; i < n; i++) {
            Map<Double, Integer> map = new HashMap<>();
            int localMax = 1;
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;
                int deltaX = points[i][0] - points[j][0];
                int deltaY = points[i][1] - points[j][1];

                Double slope = (deltaY == 0) ? Double.POSITIVE_INFINITY : (double) deltaX / deltaY;
                map.put(slope, map.getOrDefault(slope, 1) + 1);
                localMax = Math.max(localMax, map.get(slope));
            }
            max = Math.max(max, localMax);
        }
        return max;
    }
}