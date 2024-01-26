class Solution {
    public int maxPoints(int[][] points) {
        if (points.length <= 2) {
            return points.length;
        }

        int maxPoints = 1;
        for (int i = 0; i < points.length; i++) {
            Map<Double, Integer> slopeCount = new HashMap<>();
            int localMax = 1;

            for (int j = 0; j < points.length; j++) {
                if (i != j) {
                    int deltaX = points[j][0] - points[i][0];
                    int deltaY = points[j][1] - points[i][1];

                    double slope = (deltaY == 0) ? Double.POSITIVE_INFINITY : (double) deltaX / deltaY;
                    slopeCount.put(slope, slopeCount.getOrDefault(slope, 1) + 1);
                    localMax = Math.max(localMax, slopeCount.get(slope));
                }
            }
            maxPoints = Math.max(maxPoints, localMax);
        }

        return maxPoints;
    }
}
