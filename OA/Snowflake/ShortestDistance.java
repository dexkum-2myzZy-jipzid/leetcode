import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ShortestDistance {

    public static int solution(List<Integer> a, List<Integer> b) {
        int[][] points = new int[a.size()][2];
        for (int i = 0; i < a.size(); i++) {
            points[i][0] = a.get(i);
            points[i][1] = b.get(i);
        }

        Arrays.sort(points, (x, y) -> (x[0] - y[0]));

        System.out.println(Arrays.toString(points));

        return helper(points, 0, a.size() - 1);
    }

    private static int helper(int[][] points, int left, int right) {
        // right - left <= 3
        if (right - left <= 3) {
            int min = Integer.MAX_VALUE;
            for (int i = left; i < right; i++) {
                for (int j = i + 1; j <= right; j++) {
                    min = Math.min(min, distance(points[i], points[j]));
                }
            }
            return min;
        }

        int mid = (left + right) / 2;
        int[] midPoint = points[mid];

//        System.out.println(Arrays.toString(midPoint));

        int leftDis = helper(points, left, mid);
        int rightDis = helper(points, mid + 1, right);

        int dis = Math.max(leftDis, rightDis);

        int[][] stripPoints = new int[right + 1][2];
        int j = 0;
        for (int i = 0; i <= right; i++) {
            int side = points[i][0] - midPoint[0];
            if (side * side < dis) {
                stripPoints[j] = points[i];
                j += 1;
            }
        }

        return Math.min(dis, stripClosest(stripPoints, j, dis));
    }

    static int stripClosest(int[][] strip, int n, int d) {
        int min = d;
        Arrays.sort(strip, 0, n, (a, b) -> (a[1] - b[1]));

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n && (strip[j][1] - strip[i][1]) * (strip[j][1] - strip[i][1]) < min; ++j) {
                min = Math.min(min, distance(strip[i], strip[j]));
            }
        }
        return min;
    }


    private static int distance(int[] a, int[] b) {
        int dx = a[0] - b[0], dy = a[1] - b[1];
        return dx * dx + dy * dy;
    }

    public static void main(String[] args) {
        int[][] points = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};

        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();

        for (int[] point : points) {
            a.add(point[0]);
            b.add(point[1]);
        }
        System.out.println("The smallest distance is " + solution(a, b));
    }

}